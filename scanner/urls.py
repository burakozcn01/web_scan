from django.urls import path , include
from .views import nuclei_tool, nmap_tool, nikto_tool, reverse_ip_dns_tool, ip_geo_lookup, sslyze_tool

urlpatterns = [
    path('nuclei/', nuclei_tool, name='nuclei'),
    path('nmap/', nmap_tool, name='nmap'),
    path('nikto/', nikto_tool, name='nikto'),
    path('reverse-ip-dns/', reverse_ip_dns_tool, name='reverse_ip_dns'),
    path('ip-geo-lookup/', ip_geo_lookup, name='ip_geo_lookup'),
    path('sslyze/', sslyze_tool, name='sslyze')
]
