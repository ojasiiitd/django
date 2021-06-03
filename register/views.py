from django.shortcuts import render, redirect
from .forms import RegForm
import requests
from django.http import HttpResponse

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

def send_sso(response):
	print("SENDING...")
	response = requests.post(
		'http://127.0.0.1:8200/sso/login/',
		data={
				"employee_code": "TEJAS" , 
				"password": "ojas"
			}
		)
	print("SUCCESS," , response.json())
	return HttpResponse("<h1> KKKKKKKK </h1>")