from django.contrib import admin
from django.urls import path
from nmap_scanner import views

urlpatterns = [
    path('nmap/', views.nmap_scan, name='nmap_scan'),

]