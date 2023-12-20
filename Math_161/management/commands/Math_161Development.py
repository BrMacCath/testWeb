from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import numpy as np
from datetime import datetime
weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want this to make the week structure with just the command

startOfLastYear = datetime(2023,1,1)

class Command(BaseCommand):
    help= "This sets all the Weeks publishing days to the start of the year. Allows me to see the full scope."

    def handle(self, *args: Any, **options: Any) -> str | None:
        weeks = Week.objects.all()
        for week in weeks:
            print("Here")
            week.pub_date = startOfLastYear
            week.save()