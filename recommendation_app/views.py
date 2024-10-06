from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobPosting
from .serializers import JobPostingSerializer, RegisterSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully.",
        }, status=status.HTTP_201_CREATED)


class JobRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile_serializer = UserProfileSerializer(data=request.data)
        if user_profile_serializer.is_valid():
            user_profile = user_profile_serializer.save()
            recommended_jobs = self.get_job_recommendations(user_profile)
            return Response(recommended_jobs, status=status.HTTP_200_OK)
        return Response(user_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_job_recommendations(self, user_profile):
        try:
            user_skills = set(user_profile.skills)
            user_experience_level = user_profile.experience_level
            preferences = user_profile.preferences or {}

            desired_roles = set(preferences.get("desired_roles", []))
            preferred_locations = set(preferences.get("locations", []))
            preferred_job_type = preferences.get("job_type", "")

            job_postings = JobPosting.objects.filter(
                job_title__in=desired_roles,
                experience_level=user_experience_level,
                location__in=preferred_locations,
                job_type=preferred_job_type
            )

            recommended_jobs = []
            for job in job_postings:
                skill_score = self.calculate_skill_score(job.required_skills, user_skills)
                recommended_jobs.append((job, skill_score))

            # Sort jobs by skill score in descending order
            recommended_jobs.sort(key=lambda x: x[1], reverse=True)
            top_recommendations = [job for job, _ in recommended_jobs[:5]]

            output = self.format_job_recommendations(top_recommendations)
            return output if output else [{"message": "No suitable job recommendations found."}]

        except JobPosting.DoesNotExist:
            return [{"error": "Job postings not found."}]
        except Exception as e:
            return [{"error": str(e)}]

    def calculate_skill_score(self, job_skills, user_skills):
        job_skills_set = set(job_skills)
        matching_skills = user_skills.intersection(job_skills_set)

        if not job_skills_set:
            return 0

        skill_score = (len(matching_skills) / len(job_skills_set)) * 40  # Scale score to 0-40 points
        return skill_score

    def format_job_recommendations(self, jobs):
        return [
            {
                "job_title": job.job_title,
                "company": job.company,
                "required_skills": job.required_skills,
                "location": job.location,
                "job_type": job.job_type,
                "experience_level": job.experience_level
            }
            for job in jobs
        ]


class PopulateJobPostingsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            job_postings_data = request.data

            if not isinstance(job_postings_data, list):
                return Response({"error": "Invalid input format, expected a list."}, status=status.HTTP_400_BAD_REQUEST)

            required_fields = ['job_id', 'job_title', 'company', 'required_skills', 'location', 'job_type', 'experience_level']

            created_count = 0
            for job_data in job_postings_data:
                if not all(field in job_data for field in required_fields):
                    return Response({"error": f"Missing fields in job posting: {job_data}"}, status=status.HTTP_400_BAD_REQUEST)

                JobPosting.objects.update_or_create(
                    job_id=job_data['job_id'],
                    defaults={
                        'job_title': job_data['job_title'],
                        'company': job_data['company'],
                        'required_skills': job_data['required_skills'],
                        'location': job_data['location'],
                        'job_type': job_data['job_type'],
                        'experience_level': job_data['experience_level']
                    }
                )
                created_count += 1

            return Response({
                "message": f"{created_count} job postings successfully processed"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
