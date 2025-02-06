from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Menu

class MenuViewTest(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)

        # Create some Menu items for the test
        Menu.objects.create(title="Pasta", price=12.99, inventory=100)
        Menu.objects.create(title="Pizza", price=15.99, inventory=50)

        # Set the authorization header with the token for the API requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_menu_items(self):
        # Send a GET request to the menu endpoint
        response = self.client.get('/api/menu/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
