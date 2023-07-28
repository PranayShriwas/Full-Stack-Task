from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Registration
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions
from rest_framework.response import Response
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
                print(user_obj.Name)
                return render(request, 'table.html', {'form': user_obj})
            else:
                return render(request, 'login.html', {'msg': 'Password Incorrect'})
        else:
            return render(request, 'login.html', {'msg': 'Email Incorrrect'})


def table(request):
    form = Registration.objects.all()
    return render(request, 'table.html', {'form': form})

# api view for user registration


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to register


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Get username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return Response({'message': 'Login successful!', 'user_id': user.id}, status=200)
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

# api view for user list (requires authentication)


class UserListAPIView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
