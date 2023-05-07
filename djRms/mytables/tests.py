from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import user
from .serializers import userSerializer
import json


class GetUsersAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = user.objects.create(userName='test_user1', email='test_user1@example.com')
        self.user2 = user.objects.create(userName='test_user2', email='test_user2@example.com')
        self.get_users_url = reverse('users')

    def test_get_users(self):
        response = self.client.get(self.get_users_url)
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


