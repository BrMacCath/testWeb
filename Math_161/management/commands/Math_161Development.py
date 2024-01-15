from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import pytz

from django.utils import timezone
import datetime
weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want this to make the week structure with just the command

startOfLastYear = datetime.datetime(2023,1,1,tzinfo=pytz.UTC)

class Command(BaseCommand):
    help= "This sets all the Weeks publishing days to the start of the year. Allows me to see the full scope."

    def handle(self, *args: Any, **options: Any) -> str | None:
        weeks = Week.objects.all()
        releaseDate = datetime.datetime(2024,1,2,9,tzinfo=pytz.UTC)
        for week in weeks:
            week.pub_date = startOfLastYear
            week.save()
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