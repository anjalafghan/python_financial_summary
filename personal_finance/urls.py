from django.urls import path
from personal_finance import views

urlpatterns = [
    path("", views.home, name="home"),
]
