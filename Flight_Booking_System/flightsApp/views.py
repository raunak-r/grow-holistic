from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import user, airline, city, flight, booking
from .serializers import userSerializer, airlineSerializer, citySerializer, flightSerializer, bookingSerializer


# Create your views here.
def home_page(request, format=None):
    cities = city.objects.all()
    serializer = citySerializer(cities, many=True)
    # return Response(serializer.data)
    context = {
        'cities': serializer.data
    }
    return render(request, 'flightsApp/home.html', context)


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    # get all the data
    # serialize them
    # return response
    if request.method == 'GET':
        User = user.objects.all()
        serializer = userSerializer(User, many=True)
        # return Response(serializer.data)
        context = {
            'users': serializer.data
        }
        return render(request, 'flightsApp/users.html', context)
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['Get'])
def user_detail(request, pk, format=None):
    User = user.objects.filter(user_id=pk)
    serializer = bookingSerializer(User, many=True)
    return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def airline_list(request, format=None):
#     if request.method == 'GET':
#         Airline = airline.objects.all()
#         serializer = airlineSerializer(Airline, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = airlineSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def airline_list(request, Airline_id=None, format=None):
#     if request.method == 'GET':
#         if Airline_id is not None:
#             # Retrieve a specific airline by ID
#             airline_obj = airline.objects.filter(Airline_id=Airline_id)
#             serializer = airlineSerializer(airline_obj, many=True)
#             return Response(serializer.data)
#         else:
#             # Retrieve all airlines
#             airlines = airline.objects.all()
#             serializer = airlineSerializer(airlines, many=True)
#             return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = airlineSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method in ['PUT', 'PATCH', 'DELETE']:
#         airline_obj = airline.objects.get(Airline_id=Airline_id)
#         if request.method == 'PUT':
#             serializer = airlineSerializer(airline_obj, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer = airlineSerializer(
#                 airline_obj,
#                 data=request.data,
#                 partial=True
#             )
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         try:
#             airline_obj = airline.objects.get(Airline_id=Airline_id)
#         except airline.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         airline_obj.delete()
#         return Response({}, status=status.HTTP_204_NO_CONTENT)

class AirlineList(APIView):
    def get(self, request, format=None):
        airlines = airline.objects.all()
        serializer = airlineSerializer(airlines, many=True)
        # return Response(serializer.data)
        context = {
            'airlines': serializer.data
        }
        return render(request, 'flightsApp/airlines.html', context)

    def post(self, request, format=None):
        serializer = airlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirlineDetail(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            airline_obj = airline.objects.filter(Airline_id=pk)
            if airline_obj.exists():
                serializer = airlineSerializer(airline_obj, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            airlines = airline.objects.all()
            serializer = airlineSerializer(airlines, many=True)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        airline_obj = airline.objects.get(Airline_id=pk)
        serializer = airlineSerializer(airline_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        airline_obj = airline.objects.get(Airline_id=pk)
        serializer = airlineSerializer(
            airline_obj,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        airline_obj = airline.objects.get(Airline_id=pk)
        airline_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def city_list(request, format=None):
    if request.method == 'GET':
        City = city.objects.all()
        serializer = citySerializer(City, many=True)
        # return Response(serializer.data)
        context = {
            'cities': serializer.data
        }
        return render(request, 'flightsApp/cities.html', context)
    if request.method == 'POST':
        serializer = citySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def city_detail(request, pk, format=None):
    City = city.objects.filter(city_id=pk)
    serializer = citySerializer(City, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def flight_list(request, format=None):
    if request.method == 'GET':
        Flight = flight.objects.all()
        serializer = flightSerializer(Flight, many=True)
        # return Response(serializer.data)
        context = {
            'flights': serializer.data
        }
        return render(request, 'flightsApp/flights.html', context)
    if request.method == 'POST':
        serializer = flightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def flight_detail(request, pk, format=None):
    Flight = flight.objects.filter(filght_id=pk)
    serializer = flightSerializer(Flight, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def flights_between_cities(request, arr_city, dep_city, format=None):
    arrival = city.objects.get(city_name=arr_city)
    departure = city.objects.get(city_name=dep_city)
    Flight = flight.objects.filter(arr_city=arrival.city_id, des_city=departure.city_id)
    # By mistake, I created departure city as des_city, instead of dep_city, so I kept like that only
    serializer = flightSerializer(Flight, many=True)
    return Response(serializer.data)


def flights_on_date(request, format=None):
    try:
        arr_city = request.POST['arr_city']
        des_city = request.POST['des_city']
        date = request.POST['date']
    except ValueError:
        return Response({'error': 'Please Retry or try again later'})

    arr_city = city.objects.get(city_name=arr_city)
    des_city = city.objects.get(city_name=des_city)

    flights = flight.objects.filter(
        arr_city=arr_city.city_id,
        des_city=des_city.city_id,
        date=date,
    )
    if not flights:
        return render(request, 'flightsApp/flights.html', {'flightsNotFound': 'true'})

    serializer = flightSerializer(flights, many=True)
    # return Response(serializer.data)
    context = {
        'flights': serializer.data
    }
    return render(request, 'flightsApp/flights.html', context)


# @api_view(['GET', 'POST'])
# def airline_flight_list(request, name, format=None):
#     if request.method == 'GET':
#         find_airline = airline.objects.get(Airline_name=name)
#         Flight = flight.objects.filter(airline_name=find_airline.Airline_id)
#         serializer = flightSerializer(Flight, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = flightSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def booking_list(request, format=None):
    if request.method == 'GET':
        Booking = booking.objects.all()
        serializer = bookingSerializer(Booking, many=True)
        # return Response(serializer.data)
        context = {
            'bookings': serializer.data
        }
        return render(request, 'flightsApp/bookings.html', context)
    if request.method == 'POST':
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def booking_detail(request, pk, format=None):
    Booking = booking.objects.filter(user_id=pk)
    serializer = bookingSerializer(Booking, many=True)
    return Response(serializer.data)
