from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import numpy as np

weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want each week to have one instance and one instance only of 
# each weekday

class Command(BaseCommand):
    help = "Makes sure each week is done structured correctly."
    @no_translations
    def handle(self, *args: Any, **options: Any) -> str | None:
        # The first part of this is checking that each day appears once 
        # per week
        total_weeks =Week.objects.all().count()
        entries = np.zeros((total_weeks,4),dtype=int)

        for day in Day.objects.all():
            amount = weekday_with_class.count(day.day)
            if amount !=1:
                print(f"Got this {amount}")
            entries[day.week.week_num-1][weekday_with_class.index(day.day)]+=1

        correct_named_days = True
        for i in range(0,total_weeks):
            for j in range(0,4):
                if entries[i][j] != 1:
                    correct_named_days = False
        

        # This part is checking that there are no extra accidental days.
        correct_number = True
        for week in Week.objects.all():
            if week.days.all().count() != 4:
                correct_number = False
                print(f"Week {week.week_num} has {week.days.all().count()} days.")
        print(correct_named_days and correct_number) 


        
