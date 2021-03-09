from datetime import date, timedelta
from random import randrange, choice
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from menus.models import Menu, Dish
from uuid import uuid4


class Command(BaseCommand):
    help = "Handling report generation and sending"

    def add_arguments(self, parser):
        parser.add_argument('--menus', type=int)
        parser.add_argument('--dishes', type=int)
        parser.add_argument('--unique', action='store_true')

    def handle(self, *args, **options):
        menus = options['menus']
        dishes = options['dishes']
        unique = options['unique']

        menus = menus if menus or 0 > 0 else 10
        dishes = dishes if dishes or 0 > 0 else 10
        md_count = [0, 0]

        for value in range(1, menus + 1):
            try:
                if unique:
                    value = uuid4()
                Menu.objects.create(name=f"Main #{value}", description=f"Description #{value}")
                md_count[0] += 1
            except IntegrityError:
                pass

        menu_ids = Menu.objects.all().values_list("id")

        for value in range(1, dishes + 1):
            menu_id = choice(menu_ids)[0]
            instance = Dish.objects.create(
                name=f"Dish #{value}",
                description=f"Description #{value}",
                price="10.00",
                prepare_time_minutes=15,
                is_vegetarian=False,
                menu=Menu.objects.get(id=menu_id)
            )
            instance.updated_date = date.today() - timedelta(days=randrange(0, 3))
            instance.save()
            md_count[1] += 1

        self.stdout.write(f"Generated: Menu: {md_count[0]}, Dish: {md_count[1]}")





