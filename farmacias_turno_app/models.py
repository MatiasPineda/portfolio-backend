from django.db import models

from django.db import models


class Region(models.Model):
    number = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.number}: REGION DE {self.name}'


class Provincia(models.Model):
    region = models.ForeignKey(
        Region,
        related_name='provincias',
        on_delete=models.CASCADE,
    )
    number = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}, REGION DE {self.region.name}'


class Comuna(models.Model):
    provincia = models.ForeignKey(
        Provincia,
        related_name='comunas',
        on_delete=models.CASCADE,
    )
    number = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}, REGION DE {self.provincia.region.name}'


class Farmacia(models.Model):
    nombre = models.CharField(max_length=50)
    comuna = models.ForeignKey(
        Comuna,
        on_delete=models.CASCADE,
    )
    direccion = models.CharField(max_length=150)
    apertura = models.DateTimeField()
    cierre = models.DateTimeField()
    telefono = models.CharField(max_length=40, null=True)
    lat = models.DecimalField(max_digits=9,decimal_places=7, null=True)
    lng = models.DecimalField(max_digits=9,decimal_places=7, null=True)
