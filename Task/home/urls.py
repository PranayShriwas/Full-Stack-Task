from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('login_data/', views.login_data, name='login_data'),
    path('success/', views.success, name='success')
]
