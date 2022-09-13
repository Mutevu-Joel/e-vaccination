from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('staff/', views.staff, name='staff'),
    path('vaccine/', views.vaccine, name='vaccine'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('childRegistration/', views.childRegistration, name='childRegistration'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
]
