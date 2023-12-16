from django.urls import path

from . import views


app_name = "Math_161"
urlpatterns = [
    path("", views.index, name="index"),
    path("Week_<int:week_num>", views.index, name="week")
]
