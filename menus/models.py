from django.db import models

class Menu(models.Model):
    """
        Menu Model
    """

    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    """
        Dish Model
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    prepare_time_minutes = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
