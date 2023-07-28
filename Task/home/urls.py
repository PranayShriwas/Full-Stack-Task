from django.urls import path
from .import views
from .views import UserRegistrationAPIView, UserListAPIView, UserLoginAPIView
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('login_data/', views.login_data, name='login_data'),
    path('table/', views.table, name='table'),
    path('api/register/', UserRegistrationAPIView.as_view(),
         name='user-registration'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/users/', UserListAPIView.as_view(), name='user-list'),
]
