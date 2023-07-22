from django.contrib import admin
from .models import NucleiScan

@admin.register(NucleiScan)
class NucleiScanAdmin(admin.ModelAdmin):
    list_display = ('target', 'scan_output')
    search_fields = ('target', 'scan_output')
