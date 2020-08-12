from rest_framework import serializers
from .models import *


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'


class ProvinciaSerializer(serializers.ModelSerializer):
    comunas = ComunaSerializer(many=True, read_only=True)

    class Meta:
        model = Provincia
        fields = ['region', 'number', 'name', 'comunas']


class RegionSerializer(serializers.ModelSerializer):
    provincias = ProvinciaSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['number', 'name', 'provincias']


class FarmaciaTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = '__all__'
