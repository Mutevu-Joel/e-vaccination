import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control


fn = ''
ln = ''
s = ''
em = ''
pwd = ''


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    global fn, ln, s, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="!12Muuo34@", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into users Values('{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'users/register.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'users/home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="!12Muuo34@", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from users where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'users/register.html')

        else:
            return render(request, 'users/home.html', {})

    return render(request, 'users/login.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    messages.success(request, "You have successfully logged out.")
    return redirect("login")

def base(request):
    return render(request, 'users/base.html')
def staff(request):
    return render(request, 'users/staff.html')
def childRegistration(request):
    return render(request, 'users/staff.html')


# Create your views here.
