from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('childview/', views.childview, name='childview'),
    path('decorator/', views.decorator, name='decorator'),
    path('vaccine_delete/<int:pk>/', views.vaccine_delete, name='vaccine_delete'),
    path('childdelete/<int:pk>/', views.childdelete, name='childdelete'),
    path('vaccine_edit/<int:pk>/', views.vaccine_edit, name='vaccine_edit'),
    path('childedit/<int:pk>/', views.childedit, name='childedit'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('staff/', views.staff, name='staff'),
    path('vaccine1/', views.vaccine1, name='vaccine'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('childRegistration/', views.childRegistration, name='childRegistration'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
