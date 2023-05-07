import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from flightsApp.models import airline


# Create your tests here.
class AirlineListTestView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.Airline = airline.objects.create(
            Airline_name="Test Airline",
            email="customer.relations@testairline.in",
            phone="01246173838"
        )

    def test_get_airlines(self):
        url = reverse('airline-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_airlines_details(self):
        url = reverse('airline-detail', kwargs={'pk': self.Airline.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['Airline_id'], self.Airline.Airline_id)
        self.assertEqual(response.data[0]['Airline_name'], self.Airline.Airline_name)

    def test_create_airline(self):
        data = {
            "Airline_name": "Create Airline",
            "email": "customer.relations@createairline.in",
            "phone": "01246173838"
        }
        json_data = json.dumps(data)
        url = reverse('airline-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['Airline_name'], 'Create Airline')
        self.assertEqual(response.data['email'], 'customer.relations@createairline.in')
        self.assertEqual(response.data['phone'], '01246173838')

    def test_update_airline(self):
        data = {
            "Airline_name": "Update Airline",
            "email": "customer.relations@updateairline.com",
            "phone": "01246173839"
        }
        url = reverse('airline-detail', kwargs={'pk': self.Airline.pk})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Airline_name'], 'Update Airline')
        self.assertEqual(response.data['email'], 'customer.relations@updateairline.com')
        self.assertEqual(response.data['phone'], '01246173839')

    def test_delete_airline(self):
        url = reverse('airline-detail', kwargs={'pk': self.Airline.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(airline.objects.filter(pk=self.Airline.pk).exists())
