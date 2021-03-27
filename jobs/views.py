from jobs.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .models import Jobs
from .serializers import JobsSerializer

# Create your views here.



class JobList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer