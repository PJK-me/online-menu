from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from menus.models import Menu, Dish
from menus.serializers import MenuSerializer, DishSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class MenuViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class DishViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
