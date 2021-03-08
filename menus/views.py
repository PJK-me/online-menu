from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from menus.models import Menu, Dish
from menus.serializers import MenuSerializer, DishSerializer, MenuDetailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters


class MenuViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all().annotate(dish_count=Count('dish'))
    serializer_class = MenuDetailSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'dish_count']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MenuDetailSerializer
        return MenuSerializer


class DishViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filterset_fields = {
        'name': ['exact', 'contains'],
        'created_date': ['exact', 'lte', 'gte'],
        'updated_date': ['exact', 'lte', 'gte'],
    }
