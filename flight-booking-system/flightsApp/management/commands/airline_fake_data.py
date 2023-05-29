import os
import django
from django.core.management.base import BaseCommand
from flightsApp.models import airline
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            Airline_name = fake.company()
            email = fake.email()
            phone = fake.phone_number()

            # Create a new User and save it to the database
            Airline = airline.objects.create(
                Airline_name=Airline_name,
                email=email,
                phone=phone,
            )
            Airline.save()
