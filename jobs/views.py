from jobs.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .models import jobs
from .serializers import jobsSerializer

# Create your views here.

class JobList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = jobs.objects.all()
    serializer_class = jobsSerializer


class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = jobs.objects.all()
    serializer_class = jobsSerializer