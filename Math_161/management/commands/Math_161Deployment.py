from typing import Any
from django.core.management.base import BaseCommand, CommandError, no_translations
from Math_161.models import Week,Day,Quiz
import datetime
import pytz
from django.utils import timezone
weekday_with_class=["Monday","Tuesday","Wednesday","Friday"]

## Correct Structure

# I want this to make the week structure with just the command



class Command(BaseCommand):
    help= "This sets all the Weeks publishing days to the start of the year. Allows me to see the full scope."

    def handle(self, *args: Any, **options: Any) -> str | None:
        ## Week Structure
        # Sort out the release date of weeks so that they are 
        weeks = Week.objects.all().order_by("week_num")
        days=12
        startOfYear = datetime.datetime(2024,1,days,12,tzinfo=pytz.UTC)
        for week in weeks:
            week.pub_date = startOfYear
            week.save()
            startOfYear = startOfYear +datetime.timedelta(days=7)

        ## Quiz Structure
        #  Make sure weeks that have quizzes have 
        #  quiz_Boolean set to True and all others 
        #  are false.
        releaseDate = datetime.datetime(2024,1,21,9,tzinfo=pytz.UTC)
        for week in Week.objects.all():
            week.quiz_Boolean = False
        
        #  Set the release date to the correct ones
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