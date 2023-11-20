# Command: python manage.py populate_customers
import json
import os

from django.core.management import BaseCommand

from SweetToothCafe.settings import BASE_DIR
from sweet_tooth_cafe.models import Customer


class Command(BaseCommand):
    help = "Populates database with customer data from a json file"

    def handle(self, *args, **options):
        # Read from json file
        path = os.path.join(BASE_DIR, 'customers.json')
        with open(path) as file:
            customers = json.load(file)

            self.stdout.write(
                self.style.SUCCESS('Starting ingestion...')
            )

            # Loop through file and populate

            for c in customers:
                # Create customer object and save in the db
                Customer.objects.create(
                    first_name=c['first_name'],
                    last_name=c['last_name'],
                    gender=c['gender'],
                    dob=c['dob'],
                    email=c['email'],
                    is_subscribed=c['is_subscribed'],
                    profile_pic='customers/default.png',
                )

            self.stdout.write(
                self.style.SUCCESS('Ingestion completed successfully!')
            )
