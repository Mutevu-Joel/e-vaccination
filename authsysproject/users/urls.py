from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('staff/', views.staff, name='staff'),
     path('vaccine/', views.vaccine, name='vaccine'),
     path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('childRegistration/', views.childRegistration, name='childRegistration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_request, name='logout'),
]
