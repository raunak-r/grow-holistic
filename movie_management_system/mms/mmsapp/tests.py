# from django.test import TestCase
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from mmsapp.models import User

# Create your tests here.
class USERTESTVIEW(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.user=User.objects.create(
            user_name="Testing User",
            user_email="testing1234@gmail.com"
        )

    def test_get_user(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_details(self):
        url = reverse('user-detail', kwargs={'user_id': self.user.user_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.content)
        self.assertEqual(response.json()['user'][0]['user_id'], self.user.user_id)
        self.assertEqual(response.json()['user'][0]['user_name'], self.user.user_name)    

    def test_create_user(self):
        data = {
            "user_name": "Create User",
            "user_email": "customer@createauser.in"
        }
        json_data = json.dumps(data)
        url = reverse('user-list')
        response = self.client.post(url, data, format='json')
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_name'], 'Create User')
        self.assertEqual(response.data['user_email'], 'customer@createauser.in')

    def test_update_airline(self):
        data = {
            "user_name": "Update User",
            "user_email": "customer@updateuser.com"
            
        }
        url = reverse('user-detail', kwargs={'user_id': self.user.user_id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.content)
        self.assertEqual(response.json()['user_name'], 'Update User')
        self.assertEqual(response.json()['user_email'], 'customer@updateuser.com')

    def test_delete_airline(self):
        url = reverse('user-detail', kwargs={'user_id': self.user.user_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(user_id=self.user.user_id).exists())    
      
        
    