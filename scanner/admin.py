from django.contrib import admin
from .models import NucleiScan, NmapResult, NiktoScan, ReverseIPLookupResult, IPGeoLookup

@admin.register(NucleiScan)
class NucleiScanAdmin(admin.ModelAdmin):
    list_display = ('target', 'scan_output')
    search_fields = ('target', 'scan_output')


@admin.register(NmapResult)  
class NmapAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'port', 'protocol', 'state', 'service')
    list_filter = ('ip_address', 'port', 'protocol', 'state', 'service')
    search_fields = ('ip_address', 'port', 'protocol', 'state', 'service')

@admin.register(NiktoScan)
class NiktoScanAdmin(admin.ModelAdmin):
    list_display = ('target', 'created_at')
    search_fields = ('target', 'created_at')

@admin.register(ReverseIPLookupResult)
class ReverseIpDnsAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'domain_name', 'created_at')
    search_fields = ('ip_address', 'domain_name', 'created_at')

@admin.register(IPGeoLookup)
class IPGeoLookupAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'country', 'state', 'city', 'latitude', 'longitude', 'isp', 'raw_data')
    search_fields = ('ip_address', 'country', 'state', 'city', 'latitude', 'longitude', 'isp', 'raw_data')