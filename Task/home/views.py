from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Registration
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        company = request.POST['company']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(Email=email).exists():
            return render(request, 'index.html', {'msg': 'email already'})
        elif Registration.objects.filter(Phone=phone).exists():
            return render(request, 'index.html', {'msg': 'phone already'})
        else:
            Registration.objects.create(
                Name=name, Phone=phone, Email=email, Password=password, Company=company)
            return redirect('/login/')
    else:
        return HttpResponse('Email is not register')


def login_data(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Registration.objects.filter(Email=email).exists():
            user_obj = Registration.objects.get(Email=email)
            user_password = user_obj.Password
            if check_password(password, user_password):
                return redirect('/success/')
            else:
                return render(request, 'login.html', {'msg': 'Password Incorrect'})
        else:
            return render(request, 'login.html', {'msg': 'Email Incorrrect'})


def success(request):
    return render(request, 'success.html')
