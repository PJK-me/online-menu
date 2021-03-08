from django.db.models import Count
from rest_framework import viewsets
from menus.models import Menu, Dish
from menus.serializers import MenuSerializer, DishSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters


class MenuViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            self.queryset = self.queryset.annotate(dish_count=Count('dish__id')).filter(dish_count__gt=0)
        return self.queryset


class DishViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filterset_fields = {
        'name': ['exact', 'contains'],
        'created_date': ['exact', 'lte', 'gte'],
        'updated_date': ['exact', 'lte', 'gte'],
    }
