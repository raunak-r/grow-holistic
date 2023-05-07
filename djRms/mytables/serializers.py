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


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields= '__all__'

    userName = serializers.CharField(max_length=100, required=True)
    email = serializers.CharField(max_length=100, required=True)
