from django.urls import path
from .views import JobRecommendationView, PopulateJobPostingsView,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recommend/', JobRecommendationView.as_view(), name='job-recommendation'),
    path('populate/', PopulateJobPostingsView.as_view(), name='populate-jobs'),
    path('register/', RegisterView.as_view(), name='register'),
    
]