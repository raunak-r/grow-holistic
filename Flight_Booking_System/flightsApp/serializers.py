from rest_framework import serializers
from .models import user, airline, city, flight, booking

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user_id','first_name', 'last_name','dob', 'passport_number', 'email', 'phone','address']

class airlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = airline
        fields = ['Airline_id','Airline_name','email','phone']

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = ['city_id','city_code','city_name']

class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = flight
        fields = ['filght_id', 'airline_name', 'arr_city','des_city', 'date', 'number_of_seats', 'price']

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['booking_id','flight_id','user_id','order_date','total_cost']