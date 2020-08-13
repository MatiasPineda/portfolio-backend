from rest_framework import generics, viewsets
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

# End of previous version

class FarmaciasViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaTurnoSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


    # This Filter works for only one parameter, I don't need this for this project.
    #
    # def get_queryset(self):
    #     queryset = self.queryset
    #
    #     name = self.request.query_params.get('name', None)
    #     number = self.request.query_params.get('number', None)
    #     provincias = self.request.query_params.get('provincias', None)
    #     if number is not None:
    #         queryset = queryset.filter(number=number)
    #     return queryset