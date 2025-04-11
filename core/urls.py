from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import home, pricing, features, sign_up, about, custom_logout, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('pricing/', pricing, name='pricing'),
    path('features/', features, name='features'),
    path('signup/', sign_up, name='signup'),
    path('about/', about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),   
    path('dashboard/', dashboard, name='dashboard'),

]
