from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf.urls.static import static


app_name = "Misc"
urlpatterns = [
    path("", views.index, name="index"),
]
