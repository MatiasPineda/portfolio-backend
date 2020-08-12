from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name',]

class ProjectSerializer(serializers.ModelSerializer):
    skills_project = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['name', 'slug', 'live_url', 'repo_url', 'description', 'skills_project',]