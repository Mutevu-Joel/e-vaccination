import mysql.connector as sql
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import Group
from .forms import CreateUserForm



# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)








@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'users/home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    return render(request, 'users/login.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    messages.success(request, "You have successfully logged out.")
    return redirect("login")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def base(request):
    return render(request, 'users/base.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staff(request):
    return render(request, 'users/staff.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def childRegistration(request):
    return render(request, 'users/childRegistration.html')

def adminprofile(request):
    return render(request, 'users/adminprofile.html')
def vaccine(request):
    return render(request, 'users/vaccine.html')


# Create your views here.
