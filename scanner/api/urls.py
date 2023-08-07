from django.urls import path
from .views import NucleiToolAPIView, NmapToolAPIView, NiktoToolAPIView, ReverseIPDNSToolAPIView, IPGeoLookupAPIView

urlpatterns = [
    path('nuclei-api/', NucleiToolAPIView.as_view(), name='nuclei_tool_api'),
    path('nmap-api/', NmapToolAPIView.as_view(), name='nmap_tool_api'),
    path('nikto-api/', NiktoToolAPIView.as_view(), name='nikto_tool_api'),
    path('reverse-ip-dns-api/', ReverseIPDNSToolAPIView.as_view(), name='reverse_ip_dns_tool_api'),
    path('ip-geo-lookup-api/', IPGeoLookupAPIView.as_view(), name='ip_geo_lookup_api'),
]