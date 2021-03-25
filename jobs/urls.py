from django.urls import path

from .views import jobsDetails, jobsList

urlpatterns = [
    path('', jobsList.as_view(), name='job_list'),
    path('<int:pk>/', jobsDetails.as_view(), name='job_details'),
]