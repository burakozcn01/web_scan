from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuclei/', views.nuclei_tool, name='nuclei'),
    path('nuclei-api/', views.nuclei_tool_api, name='nuclei_api'), # Nuclei aracı için API URL'i
    path('nmap/', views.nmap_tool, name='nmap'),
    path('nmap-api/', views.nmap_tool_api, name='nmap_api'),       # Nmap aracı için API URL'i
    path('nikto/', views.nikto_tool, name='nikto'),
    path('nikto-api/', views.nikto_tool_api, name='nikto_api'),    # Nikto aracı için API URL'i
    path('reverse-ip-dns/', views.reverse_ip_dns_tool, name='reverse_ip_dns'),
    path('reverse-ip-dns-api/', views.reverse_ip_dns_tool_api, name='reverse_ip_dns_api'), # Reverse IP aracı için API URL'i
]
