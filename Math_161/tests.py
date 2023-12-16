from django.test import TestCase
from .models import Week,Day
# Create your tests here.

## Week Tests

# 1. Each instance of a day should appear at most once.
# 2. If it is a quiz week, the description should not be none.
# 3. Each week num is unique.
# 4. Webpage source is not saved at default.
# 5. Week title is not saved at default
# 6. There should be a way to check the pub date satifies 
# pub date cond. Need to figure that one out.
# 

class WeekTest(TestCase):
    # 1. Each instance of a day should appear at most once.
    def unique_day(self):
        pass

    # 2. If it is a quiz week, the description should not be none.
    def quiz_template(self):
        pass

    # 3. Each week num is unique.
    def unique_week_num(self):
        pass

    # 4. Webpage source is not saved at default.
    # May not need this

    # 5. Week title is not saved at default
    def title_not_at_default(self):
        pass

    # 6. There should be a way to check the pub date satifies 
    # pub date cond. Need to figure that one out.
    def pub_date_cond(self):
        pass

## Day tests
    
# 1. day description should not be at default.
#
#
    
class DayTest(TestCase):
    # 1. day description should not be at default.
    def not_default_description(self):
        pass