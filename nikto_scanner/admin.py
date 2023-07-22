from django.contrib import admin
from .models import NiktoScan

@admin.register(NiktoScan)
class NiktoScanAdmin(admin.ModelAdmin):
    list_display = ('target', 'created_at')
    search_fields = ('target', 'created_at')