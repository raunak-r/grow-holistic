import os
import django
from django.core.management.base import BaseCommand
from flightsApp.models import User
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            dob = fake.date_of_birth(minimum_age=0, maximum_age=100)
            passport_number = fake.random_int(min=100000, max=999999)
            email = fake.email()
            phone = fake.phone_number()
            address = fake.address().replace('\n', ', ')

            # Create a new User and save it to the database
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                passport_number=passport_number,
                email=email,
                phone=phone,
                address=address
            )
            user.save()
