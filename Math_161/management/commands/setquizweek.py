from typing import Any
from django.core.management.base import BaseCommand, CommandError
from Math_161.models import Week,Day,Quiz
import pytz
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help = "Notices which weeks have a quiz connected to them and sets quiz_boolean to true. Set's all other to false."
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        releaseDate = datetime.datetime(2024,1,21,9,tzinfo=pytz.UTC)
        for week in Week.objects.all():
            week.quiz_Boolean = False
        for week in Week.objects.all():
            for quiz in Quiz.objects.all():
                if quiz.week == week:
                    week.quiz_Boolean = True
                    week.save()
                    quiz.release_answers_date= releaseDate
                    quiz.save()
                    print(f"Week {week.week_num} has a quiz. The answer key will be released on {quiz.release_answers_date}.")
                    break
            releaseDate = releaseDate +datetime.timedelta(days=7)