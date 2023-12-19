from typing import Any
from django.core.management.base import BaseCommand, CommandError
from Math_161.models import Week,Day,Quiz


class Command(BaseCommand):
    help = "Notices which weeks have a quiz connected to them and sets quiz_boolean to true. Set's all other to false."
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        for week in Week.objects.all():
            week.quiz_Boolean = False
        for week in Week.objects.all():
            for quiz in Quiz.objects.all():
                if quiz.week.week_num == week.week_num:
                    week.quiz_Boolean = True
                    print(f"Week {week.week_num} has a quiz")
                    break