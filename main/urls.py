from django.urls import path
from . import views

urlpatterns = [
    path("lists/<int:id>" , views.index , name="index"),
]