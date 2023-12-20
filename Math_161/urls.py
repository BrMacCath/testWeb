from django.urls import path

from . import views


app_name = "Math_161"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("Week_<int:week_num>", views.week, name="week"),
    path("Week_<int:week_num>/Quiz", views.quiz, name="quiz"),
    path("Week_<int:week_num>/<str:day>", views.day, name="day"),
    
]
