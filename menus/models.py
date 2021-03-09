from django.db import models


class Menu(models.Model):
    """
        Menu Model
    """

    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    """
        Dish Model
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    prepare_time_minutes = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} in {self.menu}" if self.menu is not None else f"{self.name} without Menu"
