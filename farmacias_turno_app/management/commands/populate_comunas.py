from farmacias_turno_app.models import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    manual_fix = {
        # Need this to fix some inconsistencies in naming convention between the file and the api
        # FILE : API
        'LLAILLAY': 'LLAY LLAY',
        'TILTIL': 'TIL-TIL',
        'AISEN': 'AYSEN',
        'COIHAIQUE': 'COYHAIQUE',
        'NATALES': 'PUERTO NATALES',
        'MARCHIHUE': 'MARCHIGUE',
        'MOSTAZAL': 'SAN FRANCISCO DE MOSTAZAL',
        'PAIGUANO': 'PAIHUANO',
        'SAAVEDRA': 'PUERTO SAAVEDRA',
        'CALERA': 'LA CALERA'
    }


    def formatting_data(self):
        """Gets data from codigos.txt and formats them into a list of dictionaries"""
        with open('farmacias_turno_app/management/commands/codigos.txt', 'r') as f:
            data = eval(f.read())
        data[0] = [word.title() for word in data[0]]
        for comuna in data[1:]:
            comuna[1], comuna[3], comuna[5] = comuna[1].upper(), comuna[3].upper(), comuna[5].upper()
            if comuna[5] in self.manual_fix:
                comuna[5] = self.manual_fix[comuna[5]]
        d = [dict(zip(data[0], i)) for i in data[1:]]
        return d


    def populate_db(self):
        """Calls formatting_data function, then populates database"""
        data = self.formatting_data()
        created = False
        for element in data:
            try:
                r = Region.objects.create(number=element['Codigo Region'], name=element['Nombre Region'])
            except:
                r = Region.objects.get(pk=element['Codigo Region'])
            try:
                p = Provincia.objects.create(region=r, number=element['Codigo Provincia'], name=element['Nombre Provincia'])
            except:
                p = Provincia.objects.get(number=element['Codigo Provincia'])
            try:
                c = Comuna.objects.create(provincia=p, number=element['Codigo Comuna 2017'], name=element['Nombre Comuna'])
            except Exception as e:
                created = True
        if created:
            print('DB already populated')
        else:
            print("Success populating Region, Provincia, Comuna")

    def handle(self, *args, **options):
        self.populate_db()
        self.stdout.write(f"Comunas Registradas")
