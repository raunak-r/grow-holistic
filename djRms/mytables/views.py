from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status
from rest_framework.generics import UpdateAPIView

from .models import rest, user, item, discount, order
from .serializers import RestSerializer, itemSerializer, userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError


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
# @api_view(['GET'])
# def get_users(request):
#     users=user.objects.all()
#     serializer= usersSerializer(users, many=True)
#     return Response(serializer.data)
# @api_view(['POST'])
# def create_user(request):
#     serializer = userSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_users(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

class create_user(generics.CreateAPIView):
    serializer_class = userSerializer


def delete_user(request, pk):
    User = get_object_or_404(user, pk=pk)
    User.delete()
    return HttpResponse("User deleted successfully")


# @require_http_methods(["PUT"])
# def update_user(request, pk):
#     User = get_object_or_404(user, pk=pk)
#     username = request.POST.get('userName')
#     email = request.POST.get('email')
#
#     if username is None and email is None:
#         return JsonResponse({'error': 'At least one field is required.'}, status=400)
#
#     if username is not None:
#         User.userName = username
#
#     if email is not None:
#         User.email = email
#
#     try:
#         User.full_clean()
#         User.save()
#         return HttpResponse("User updated successfully")
#     except ValidationError as e:
#         return JsonResponse({'error': e.message}, status=400)

class update_user(UpdateAPIView):
    serializer_class = userSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(user, pk=pk)
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()