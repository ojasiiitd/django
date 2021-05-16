from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item , ToDoList
from .forms import CreateNewList
# Create your views here.

def index(response , id):
    ls = ToDoList.objects.get(id=id)
    try:
        items = ls.item_set.get(id=1)
    except:
        items = Item(text="No Items in List yet" , complete=False)
    return render(response , "main/list.html" , {"ls":ls})

def home(response):
    return render(response , "main/home.html")

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/lists/%i" %(t.id))

    else:
        form = CreateNewList()
    return render(response , "main/create.html" , {"form":form})