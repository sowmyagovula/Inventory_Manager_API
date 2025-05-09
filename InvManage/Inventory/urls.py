from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name= "register"),
    path('inventory_manage/', views.inventory_manage, name='inventory_manage'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('account_details/', views.account_details, name='account_details'),
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)