from rest_framework import serializers

from .models import jobs


class jobsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'company', 'job_title', 'salary', 'notes', 'created_at')
        model = jobs