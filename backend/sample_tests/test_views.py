from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.test import TestCase
from django.conf import settings

class InstalledAppsTestCase(TestCase):
    def test_installed_apps(self):
        actual_apps = settings.INSTALLED_APPS

        if 'myapp.apps.MyAppConfig' in actual_apps:
            contain = True

        self.assertTrue(contain)


class HomeViewTestCase(APITestCase):

    def test_home_view_authenticated(self):
        # Test when the user is authenticated
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


