# Generated by Django 4.2 on 2023-04-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_org', '0002_customer_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['Booking_id']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['customer_id']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_name']},
        ),
    ]