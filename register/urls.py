from django.urls import path
from . import views

urlpatterns = [
    path("" , views.reg , name="reg"),
    path("req/" , views.send_sso , name="sso"),
]