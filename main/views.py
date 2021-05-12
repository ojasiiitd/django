from typing import Text
from django.shortcuts import render 
from django.http import HttpResponse
from .models import Item , ToDoList
# Create your views here.

def index(response , id):
    ls = ToDoList.objects.get(id=id)
    try:
        items = ls.item_set.get(id=1)
    except:
        items = Item(text="No Items in List yet" , complete=False)
    return HttpResponse("<h1> %s </h1> <br> %s " %(ls.name , items.text))