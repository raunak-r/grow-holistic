import os
import django
from django.core.management.base import BaseCommand
from django.db.models import Max
from flightsApp.models import flight, airline, city
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            airline_name = airline.objects.order_by('?').first()
            arr_city = city.objects.order_by('?').first()
            des_city = city.objects.exclude(pk=arr_city.pk).order_by('?').first()
            date = fake.date_between(start_date='-30d', end_date='+30d')
            number_of_seats = random.randint(100, 400)
            price = random.randint(1000, 5000)

            # Create a new User and save it to the database
            Flight = flight.objects.create(
                airline_name=airline_name,
                arr_city=arr_city,
                des_city=des_city,
                date=date,
                number_of_seats=number_of_seats,
                price=price,
            )
            Flight.save()
