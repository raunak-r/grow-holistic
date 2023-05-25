from rest_framework import serializers
from .models import User, airline, city, flight, booking


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class airlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = airline
        fields = '__all__'


class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__'


class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = flight
        fields = '__all__'


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
