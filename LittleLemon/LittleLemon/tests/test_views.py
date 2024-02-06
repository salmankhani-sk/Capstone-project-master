from django.test import TestCase
from restaurant.models import Menu
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(
            title='Menu 1', price=10.99, inventory=10)
        self.menu2 = Menu.objects.create(
            title='Menu 2', price=15.99, inventory=20)
        self.menu3 = Menu.objects.create(
            title='Menu 3', price=20.99, inventory=30)

        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/restaurant/menu/items')

        response_data = json.loads(response.content)

        test_data = [
            {'id': self.menu1.id, 'title': self.menu1.title, 'price': str(
                self.menu1.price), 'inventory': self.menu1.inventory},
            {'id': self.menu2.id, 'title': self.menu2.title, 'price': str(
                self.menu2.price), 'inventory': self.menu2.inventory},
            {'id': self.menu3.id, 'title': self.menu3.title, 'price': str(
                self.menu3.price), 'inventory': self.menu3.inventory},
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, test_data)
