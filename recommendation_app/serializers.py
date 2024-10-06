from rest_framework import serializers
from .models import UserProfile, JobPosting
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class PreferencesSerializer(serializers.Serializer):
    desired_roles = serializers.ListField(child=serializers.CharField())
    locations = serializers.ListField(child=serializers.CharField())
    job_type = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    preferences = PreferencesSerializer(required=False)  # Make it optional

    class Meta:
        model = UserProfile
        fields = ['name', 'skills', 'experience_level', 'preferences']

    def create(self, validated_data):
        preferences_data = validated_data.pop('preferences', {})
        
        user_profile = UserProfile.objects.create(**validated_data)
        
        # Ensure preferences are not null
        if preferences_data:
            user_profile.preferences = preferences_data
        user_profile.save()
        
        return user_profile

    def update(self, instance, validated_data):
        preferences_data = validated_data.pop('preferences', {})
        
        instance.name = validated_data.get('name', instance.name)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.experience_level = validated_data.get('experience_level', instance.experience_level)

        # Update preferences if provided
        if preferences_data:
            instance.preferences = preferences_data

        instance.save()
        return instance

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'  # Or specify individual fields if preferred