from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import *

routers = routers.SimpleRouter()

urlpatterns = [
    path('projects/', ListProject.as_view(), name='ListProject'),
    path('projects/images/', ListImageProject.as_view(), name='ListImageProject'),
    path('projects/<int:pk>/', DetailProject.as_view(), name='DetailProject'),
]