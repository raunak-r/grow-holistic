import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlightMngSys.settings")
django.setup()

from django.core.management.base import BaseCommand
from mmsapp.models import User
from faker import Faker


class Command(BaseCommand):
    help = 'Loads fake data into the database.'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            user_name = fake.user_name()
            user_email = fake.email()


            # Create a new User and save it to the database
            user = User.objects.create(
                user_name=user_name,
                user_email=user_email
            )
            user.save()