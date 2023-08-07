from django.urls import path , include
from .views import nuclei_tool, nmap_tool, nikto_tool, reverse_ip_dns_tool, ip_geo_lookup

urlpatterns = [
    path('nuclei-scan/', nuclei_tool, name='nuclei'),
    path('nmap-scan/', nmap_tool, name='nmap'),
    path('nikto-scan/', nikto_tool, name='nikto'),
    path('reverse-ip-dns-scan/', reverse_ip_dns_tool, name='reverse_ip_dns'),
    path('ip-geo-lookup-scan/', ip_geo_lookup, name='ip_geo_lookup'),

]
