from django.urls import path

from . import views

app_name="WebsiteProgress"
urlpatterns = [
    path("", views.index, name="index"),
    path("Phase_<int:phase_id>/", views.phase, name="phase"),
]