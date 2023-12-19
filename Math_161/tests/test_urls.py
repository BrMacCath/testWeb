from django.test import SimpleTestCase
from django.urls import resolve,reverse
from Math_161.views import index,week,day,quiz,IndexView
from pathlib import Path

# from import db
# I am going to make sure that the urls are done correctly

class testUrls(SimpleTestCase):
    # This is to test the index website
    def test_index_is_resolved(self):
        url = reverse("Math_161:index")
        print(resolve(url))
        print(url)
        print(IndexView)
        self.assertEquals(resolve(url).func,IndexView)

    def test_week_is_resolved(self):
        url = reverse("Math_161:week",kwargs={"week_num":1})
        self.assertEquals(resolve(url).func,week)
    
    def test_day_is_resolved(self):
        url = reverse("Math_161:day",kwargs={"week_num":1,"day":"Monday"})
        self.assertEquals(resolve(url).func,day)

    # def test_quiz_is_resolved(self):
    #     url = reverse("Math_161:quiz",kwargs={"quiz_num":1})
    #     self.assertEquals(resolve(url).func,quiz)
    
    