from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuclei/', views.nuclei_tool, name='nuclei'),
    path('nmap/', views.nmap_tool, name='nmap'),
    path('nikto/', views.nikto_tool, name='nikto'),
    path('reverse-ip-dns/', views.reverse_ip_dns_tool, name='reverse_ip_dns'),
    path('ip-geo-lookup/', views.ip_geo_lookup, name='ip_geo_lookup'),  # IP Geolocation Lookup için yol
    path('nmap-api/', views.nmap_tool_api, name='nmap_tool_api'),  # Nmap API için yol
    path('nuclei-api/', views.nuclei_tool_api, name='nuclei_tool_api'),  # Nuclei API için yol
    path('nikto-api/', views.nikto_tool_api, name='nikto_tool_api'),  # Nikto API için yol
    path('reverse-ip-dns-api/', views.reverse_ip_dns_tool_api, name='reverse_ip_dns_tool_api'),  # Reverse IP-DNS API için yol
    path('ip-geo-lookup-api/', views.ip_geo_lookup_api, name='ip_geo_lookup_api'),  # IP Geolocation Lookup API için yol
]
