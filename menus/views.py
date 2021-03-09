from django.db.models import Count
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from menus.models import Menu, Dish
from menus.serializers import MenuSerializer, DishSerializer, MenuDetailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import filters


class MenuViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all().annotate(dish_count=Count('dish'))
    serializer_class = MenuDetailSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'dish_count']
    filterset_fields = {
        'name': ['exact', 'contains'],
        'created_date': ['exact', 'lte', 'gte'],
        'updated_date': ['exact', 'lte', 'gte'],
    }

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MenuDetailSerializer
        return MenuSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            self.queryset = self.queryset.filter(dish_count__gt=0)
        return self.queryset


class DishViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filterset_fields = {
        'name': ['exact', 'contains'],
        'created_date': ['exact', 'lte', 'gte'],
        'updated_date': ['exact', 'lte', 'gte'],
    }
