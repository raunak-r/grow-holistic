from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import rest, user, item, discount, order
from .serializers import RestSerializer, itemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_queryset(request, city_name, format=None):
    queryset = rest.objects.filter(city=city_name)
    serializer = RestSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items(request, format=None):
    items = item.objects.all()
    serializer = itemSerializer(items, many=True)
    return Response(serializer.data)


def get_itemsbyrests(request, rest_name, format=None):
    rest_obj = rest.objects.get(restName=rest_name)
    items = item.objects.filter(restId=rest_obj.restId)
    item_list = []
    for item_obj in items:
        item_dict = {
            "itemId": item_obj.itemId,
            "itemName": item_obj.itemName,
            "itemPrice": item_obj.itemPrice,
            "restName": item_obj.restId.restName
        }
        item_list.append(item_dict)

    # Return the item data as a JSON response
    return JsonResponse(item_list, safe=False)

    # serializer = itemSerializer(items, many=True)
    # return Response(serializer.data)
