from datetime import date, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from app import settings
from menus.models import Dish
from django.contrib.auth.models import User
from django.db.models import Q


class Command(BaseCommand):
    help = "Handling report generation and sending"

    def handle(self, *args, **options):
        prev_day = date.today() - timedelta(days=1)
        recent_dishes = Dish.objects.filter(Q(created_date=prev_day) | Q(updated_date=prev_day))

        if recent_dishes:
            dish_list = ",\b".join([f"{i.get('name')}" for i in recent_dishes.values("name", "description")])
            emails = [i.get("email") for i in User.objects.all().values("email")]

            send_mail(
                'Online Menu - New and modified dishes',
                f"List of dishes created/modified yesterday:\b{dish_list}",
                settings.EMAIL_HOST_USER,
                emails,
                fail_silently=False,
            )

            self.stdout.write("E-mail Reports were sent.")

        else:

            self.stdout.write("No New Report Available")
