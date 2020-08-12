import json
import requests
from farmacias_turno_app.models import Farmacia, Comuna
from datetime import datetime, timedelta
import pytz
from decimal import Decimal
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Refreshes data of farmacias_turno_app_farmacia'

    # API url
    url = "https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos"

    req = requests.get(url)
    decoded_data = req.content.decode('utf-8-sig')  # Don't understand this step

    data = json.loads(decoded_data)

    def delete_info_farmacias(self):
        Farmacia.objects.all().delete()

    def populate_farmacias_turno(self):
        for element in self.data:
            f = Farmacia()
            f.nombre = element['local_nombre']
            f.comuna = Comuna.objects.get(name=element['comuna_nombre'])
            f.direccion = element['local_direccion']

            hora_apertura = datetime.strptime(f"{element['fecha']} {element['funcionamiento_hora_apertura']}",
                                              '%Y-%m-%d '
                                              '%H:%M:%S')
            f.apertura = hora_apertura.replace(tzinfo=pytz.UTC)

            hora_cierre = datetime.strptime(f"{element['fecha']} {element['funcionamiento_hora_cierre']}",
                                            '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            f.cierre = hora_cierre.replace(tzinfo=pytz.UTC)

            f.telefono = element['local_telefono']
            if element['local_lat'].replace(".", "0").replace(",", "0").replace("-", "0").isalnum() \
                    and element['local_lng'].replace(".", "0").replace(",", "0").replace("-", "0").isalnum():
                try:
                    f.lat = Decimal(element['local_lat'].replace(",", ".")[:8])
                    f.lng = Decimal(element['local_lng'].replace(",", ".")[:8])
                except Exception:
                    print(Exception)
            f.save()

    def handle(self, *args, **options):
        self.delete_info_farmacias()
        self.populate_farmacias_turno()
        self.stdout.write(f"Farmacias actualizadas")
