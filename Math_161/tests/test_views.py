from django.test import TestCase,Client
from django.urls import reverse
from Math_161.models import Day


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse("Math_161:index")
        self.week_url = reverse("Math_161:week",kwargs={"week_num":1})
        self.day_url  = reverse("Math_161:day",kwargs={"week_num":1,"day":"Monday"})
        self.quiz_url = reverse("Math_161:quiz",kwargs={"quiz_num":1})

    def test_index_views(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"Math_161/index.html")

    # def test_week_views(self):
    #     response = self.client.get(self.week_url)
    #     print(response.status_code)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,"Math_161/week.html")

    def test_index_views(self):
        response = self.client.get(self.day_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"Math_161/day.html")

    # def test_index_views(self):
    #     response = self.client.get(self.index_url)
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,"Math_161/index.html")