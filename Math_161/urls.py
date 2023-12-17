from django.urls import path

from . import views


app_name = "Math_161"
urlpatterns = [
    path("", views.index, name="index"),
    path("Week_<int:week_num>", views.week, name="week"),
    path("Week_<int:week_num>/<str:day>", views.day, name="day")
]