from django.shortcuts import render
from rest_framework import generics
from .models import rest, user, item, discount, order
from .serializers import RestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_queryset(request, city_name, format=None):
    queryset = rest.objects.filter(city=city_name)
    serializer = RestSerializer(queryset, many=True)
    return Response(serializer.data)
