from django.contrib import admin
from django.urls import path
from nuclei_scanner import views



urlpatterns = [
    path('nuclei/', views.nuclei_scan, name='nuclei_scan'),

]