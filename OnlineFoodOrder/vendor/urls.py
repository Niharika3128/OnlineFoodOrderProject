"""OnlineFoodOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from vendor import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='vendor/login.html'),name='vendor_main'),
    path('open_register/',TemplateView.as_view(template_name='vendor/register.html'),name='open_register'),
    path('vendor_login_check/',views.vendorLoginCheck,name='vendor_login_check'),
    path('welcome_vendor/',views.vendor_home,name='welcome_vendor'),
    path('save_vendor/',views.save_vendor,name='save_vendor'),

]
