from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name',]

class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImages
        fields = ['image']


class ProjectSerializer(serializers.ModelSerializer):
    skills_project = SkillSerializer(many=True, read_only=True)
    imagenes = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['name', 'slug', 'live_url', 'repo_url', 'description', 'skills_project', 'imagenes']
