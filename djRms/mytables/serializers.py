from rest_framework import serializers
from .models import rest, user, item, discount, order


class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = rest
        fields = '__all__'

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'