import json
import os

from django.core.management import BaseCommand

from SweetToothCafe.settings import BASE_DIR
from sweet_tooth_cafe.models import Candy


class Command(BaseCommand):
    help = 'Populates database with candy data from json file'

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'candy.json')
        with open(path) as file:
            candy = json.load(file)

            self.stdout.write(
                self.style.SUCCESS('Starting to ingest the data...')
            )

            for c in candy:
                Candy.objects.create(
                    name=c['name'],
                    cost=c['cost'],
                    price=c['price'],
                    brand=c['brand'],
                    desc=c['desc'],

                )

            self.stdout.write(
                self.style.SUCCESS("Data ingested successfully!")
            )