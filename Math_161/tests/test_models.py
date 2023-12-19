from django.test import TestCase
from Math_161.models import Week,Day
# Create your tests here.

## Week Tests

# 1. Each instance of a day should appear at most once.
# This is handled in commands as we need to access model data
# and you cannot do that in here.
# 2. If it is a quiz week, the description should not be none.
# This is handled in commands as we need to access model data
# and you cannot do that in here.
# 3. Each week num is unique.
# This is handled in commands as we need to access model data
# and you cannot do that in here.
# 4. Webpage source is not saved at default.
# This is handled in commands as we need to access model data
# and you cannot do that in here.
# 5. Week title is not saved at default
# 6. There should be a way to check the pub date satifies 
# pub date cond. Need to figure that one out.
# 

class WeekTest(TestCase):

    def setUp(self):
        print("This")
        self.Weeks = Week.objects.all()
        self.Days = Day.objects.all()
    # 1. Each instance of a day should appear once a week.
    def test_unique_day(self):
        print("Here")
        
        print(self.Weeks)
        for week in Week.objects.all():
            print("Test")
        for day in self.Days:
            count = 0
            print("Here")
            for week in self.Weeks:
                if day.week.week_num == week.week_num:
                    count += 1
                    print("Yes")
            self.assertSetEqual(count,2)


    # 2. If it is a quiz week, the description should not be none.
    def test_quiz_template(self):
        # Weeks = Week.objects.all()
        # for week in Weeks:
        #     if week.has_quiz:
        #         self.assertNotEqual()
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


## Quiz Tests