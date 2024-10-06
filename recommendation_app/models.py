from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    skills = models.JSONField()
    experience_level = models.CharField(max_length=20)
    
    # Nesting preferences into a single JSONField
    preferences = models.JSONField(null=True, blank=True)  # This will store desired_roles, locations, and job_type

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    job_id = models.IntegerField(unique=True)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    required_skills = models.JSONField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20)
    experience_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.job_title} at {self.company}"
