from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1> OJASVA SAXENA </h1>")

def view1(response):
    return HttpResponse("<h2> NEW VIEW </h2>")