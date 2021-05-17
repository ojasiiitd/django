from django.shortcuts import render, redirect
from .forms import RegForm

# Create your views here.

def reg(response):
    if response.method == "POST":
        form = RegForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegForm()

    return render(response , "register/reg.html" , {"form":form})