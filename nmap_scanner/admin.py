from django.contrib import admin
from nmap_scanner.models import NmapResult  

@admin.register(NmapResult)  
class NmapAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'port', 'protocol', 'state', 'service')
    list_filter = ('ip_address', 'port', 'protocol', 'state', 'service')
    search_fields = ('ip_address', 'port', 'protocol', 'state', 'service')
