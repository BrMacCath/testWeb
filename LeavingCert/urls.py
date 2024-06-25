from django.urls import path

from . import views

app_name = "LeavingCert"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("<str:sub_name>",views.subPage,name="sub"),
    path("<str:sub_name>/<str:topic_name>",views.topicPage,name="topic"),
    path("<str:sub_name>/<str:topic_name>/<str:unit_name>",views.topicPage,name="unit")
]