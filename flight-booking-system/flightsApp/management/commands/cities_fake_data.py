import os
import django
from django.core.management.base import BaseCommand
from flightsApp.models import city
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            city_name = fake.unique.city()
            city_code = city_name[:1].upper() + ''.join(random.choices(city_name.upper(), k=2))

            # Create a new User and save it to the database
            City = city.objects.create(
                city_name=city_name,
                city_code=city_code,
            )
            City.save()
