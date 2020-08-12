from django.urls import path
from rest_framework import routers

from .views import *

routers = routers.SimpleRouter()

urlpatterns = [
    path('projects/', ListProject.as_view(), name='ListProject'),
    path('projects/<int:pk>/', DetailProject.as_view(), name='DetailProject'),
]