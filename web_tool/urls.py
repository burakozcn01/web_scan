from django.contrib import admin
from django.urls import path , include
from scanner import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scanner.urls')),
    path('', include('scanner.api.urls')),

]