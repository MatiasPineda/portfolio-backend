from rest_framework import generics
from .serializer import *


class ListRegion(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DetailComuna(generics.RetrieveAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class ListFarmaciasTurno(generics.ListAPIView):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaTurnoSerializer


class DetailFarmaciasTurno(generics.RetrieveAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer