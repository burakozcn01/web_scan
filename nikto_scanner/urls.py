from django.contrib import admin
from django.urls import path
from nikto_scanner import views

urlpatterns = [
    path('nikto/', views.NiktoScan, name='nikto_scan'),

]