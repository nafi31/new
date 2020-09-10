from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import render, redirect
# Create your views here.
def register(response):
    if response.method=="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            x=form.save()
            x.save()
            return redirect("/login")
    else:
        form = RegisterForm()
        
    return render(response,'register/register.html',{"form":form})