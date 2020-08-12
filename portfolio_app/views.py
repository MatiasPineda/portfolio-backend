from rest_framework import generics
from .serializer import *


class ListProject(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DetailProject(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer