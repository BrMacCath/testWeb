from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations, CommandParser
from Math_161.models import Week,Day,Quiz
import numpy as np

weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want each week to have one instance and one instance only of 
# each weekday

class Command(BaseCommand):
    help="Adds a quiz to the week depending on the week num you give it."
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("week_num",type=int)

    def handle(self, *args,**options ) -> str | None:
        week_num = options["week_num"]
        week_chosen = Week.objects.get(week_num=week_num)
        quiz_num = Quiz.objects.all().count()+1
        week_chosen.quiz.create(quiz_num=quiz_num)
        week_chosen.save()