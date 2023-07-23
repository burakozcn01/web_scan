from django.contrib import admin
from django.urls import path
from scanner import views



urlpatterns = [
    path('nuclei/', views.nuclei_scan, name='nuclei_scan'),
    path('nmap/', views.nmap_scan, name='nmap_scan'),
    path('nikto/', views.nikto_scan, name='nikto_scan'),
    path('reverse_ip_lookup/', views.reverse_ip_lookup, name='reverse_ip_lookup'),
]