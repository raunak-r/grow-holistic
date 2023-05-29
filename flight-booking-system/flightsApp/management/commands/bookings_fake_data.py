import os
import django
from django.core.management.base import BaseCommand
from django.db.models import Max
from flightsApp.models import flight, airline, User, booking
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            flight_id = flight.objects.order_by('?').first()
            user_id = User.objects.order_by('?').first()
            order_date = fake.date_between(start_date='-60d', end_date='+0d')
            total_cost = random.randint(1000, 15000)

            # Create a new User and save it to the database
            Booking = booking.objects.create(
                flight_id=flight_id,
                user_id=user_id,
                order_date=order_date,
                total_cost=total_cost,
            )
            Booking.save()
