from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user, airline, city, flight, booking
from .serializers import userSerializer, airlineSerializer, citySerializer, flightSerializer, bookingSerializer

# Create your views here.
@api_view(['GET'])
def user_list(request, format=None):
        #get all the data
        #serialize them
        #return response
    User = user.objects.all()
    serializer = userSerializer(User, many=True)
    return Response(serializer.data)

def airline_list(request, format=None):
    Airline = airline.objects.all()
    serializer = airlineSerializer(Airline, many=True)
    return Response(serializer.data)
        
def city_list(request, format=None):
    City = city.objects.all()
    serializer = citySerializer(City, many=True)
    return Response(serializer.data)
        
def flight_list(request, format=None):
    Flight = flight.objects.all()
    serializer = flightSerializer(Flight, many=True)
    return Response(serializer.data)

def target_flight_list(request, arr_city, dep_city, format=None):
    arrival = city.objects.get(city_name=arr_city)
    departure = city.objects.get(city_name=dep_city)
    Flight = flight.objects.filter(arr_city=arrival.city_id, des_city=departure.city_id) #by mistake i created departure city as des_city instead of dep_city, so i kept like that only
    serializer = flightSerializer(Flight, many=True)
    return Response(serializer.data)

def airline_flight_list(request, name, format=None):
    find_airline = airline.objects.get(Airline_name=name)
    Flight = flight.objects.filter(airline_name=find_airline.Airline_id)
    serializer = flightSerializer(Flight, many=True)
    return Response(serializer.data)
           
def booking_list(request, format=None):
    Booking = booking.objects.all()
    serializer = bookingSerializer(Booking, many=True)
    return Response(serializer.data)
    
def user_booking_list(request, id, format=None):
    booking.objects.filter(user_id = id)
    Booking = booking.objects.all()
    serializer = bookingSerializer(Booking, many=True)
    return Response(serializer.data)
    
@api_view(['PUT'])
def create_user(request, format=None):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

def create_booking(request, format=None):
    serializer = bookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)