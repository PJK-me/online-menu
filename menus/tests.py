from django.contrib.auth import get_user_model
from django.db.models import Count
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from menus.models import Menu, Dish
from menus.serializers import MenuSerializer, MenuDetailSerializer, DishSerializer


class MenuApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test',
            'passpass123'
        )

        Menu.objects.create(name='Main', description="main desc")
        Menu.objects.create(name='Other', description="other desc")
        Menu.objects.create(name='Next', description="next desc")

    def test_retrieve_menu_list_unauthorized(self):
        response = self.client.get("/api/v1/menu/")
        ingredients = Menu.objects.all().annotate(dish_count=Count('dish')).filter(dish_count__gt=0).order_by("-id")
        serializer = MenuSerializer(ingredients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_menu_list_authorized(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/menu/")
        ingredients = Menu.objects.all().annotate(dish_count=Count('dish'))
        serializer = MenuSerializer(ingredients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_unauthorized(self):
        body = {
            'name': 'Another',
            "description": "another menu"
        }

        response = self.client.post("/api/v1/menu/", body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        exists = Menu.objects.filter(
            name=body['name'],
            description=body['description'],
        ).exists()
        self.assertFalse(exists)

    def test_create_menu_authorized(self):
        self.client.force_authenticate(self.user)
        body = {
            'name': 'Another',
            "description": "another menu"
        }

        response = self.client.post("/api/v1/menu/", body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exists = Menu.objects.filter(
            name=body['name'],
            description=body['description'],
        ).exists()
        self.assertTrue(exists)

