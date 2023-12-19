from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import numpy as np
from datetime import datetime
weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want this to make the week structure with just the command

class Command(BaseCommand):
    help ="This should create a week with the Day foreign keys filled out."

    def handle(self, *args: Any, **options: Any) -> str | None:
        # The plus one is because I want to create the next week number.
        week_num = Week.objects.all().count()+1
        now = datetime.now()
        new_week = Week.objects.create(week_num=week_num,pub_date=now)
        for day in weekday_with_class:
            new_week.days.create(week=new_week,day=day)
        new_week.save()
        print("Created a new week instance.")

        pass