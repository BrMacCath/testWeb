from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf.urls.static import static


app_name = "Lin"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:weight>",views.topic_page,name="topic")
]
