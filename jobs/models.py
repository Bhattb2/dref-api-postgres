from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Jobs(models.Model):
    author = models.ForeignKey(User(), on_delete=models.CASCADE)
    company = models.CharField(max_length=64)
    job_title = models.TextField()
    salary = models.IntegerField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company