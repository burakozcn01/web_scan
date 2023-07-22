from django.contrib import admin
from django.urls import path , include
from nuclei_scanner.views import nuclei_scan
from nmap_scanner.views import nmap_scan
from nikto_scanner.views import nikto_scan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nmap_scanner.urls')),
    path('', include('nuclei_scanner.urls')),
    path('', include('nikto_scanner.urls')),

]