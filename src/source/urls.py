from django.urls import path
from source import views

urlpatterns = [
    path("", views.home, name="home"),
]
