from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import numpy as np
import datetime
weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want this to make the week structure with just the command



class Command(BaseCommand):
    help= "This sets all the Weeks publishing days to the start of the year. Allows me to see the full scope."

    def handle(self, *args: Any, **options: Any) -> str | None:
        weeks = Week.objects.all().order_by("week_num")
        days=14
        startOfYear = datetime.datetime(2024,1,days)
        for week in weeks:
            print("Here")
            week.pub_date = startOfYear
            week.save()
            days +=7
            startOfYear = datetime.datetime(2024,1,days)