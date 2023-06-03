from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from backend.urls import urlpatterns


class HomeViewTestCase(APITestCase):

    def test_home_view_authenticated(self):
        # Test when the user is authenticated
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_view_content(self):
        # Test when the user is authenticated
        response = self.client.get(reverse('home'))
        self.assertEqual(response.json(), {"message": "Welcome to Django!"})

    def test_urlpatterns(self):
        # Test when the user is authenticated
        response = len(urlpatterns)
        self.assertEqual(response, 2)


