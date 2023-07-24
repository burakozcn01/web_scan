from django.db import models

class NucleiScan(models.Model):
    target = models.CharField(max_length=100) 
    scan_output = models.TextField()

    def __str__(self):
        return self.target

class NmapResult(models.Model):
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip_address}:{self.port}"
    
class NiktoScan(models.Model):
    target = models.CharField(max_length=255)
    scan_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nikto Scan for {self.target} at {self.created_at}"
    
class ReverseIPLookupResult(models.Model):
    ip_address = models.GenericIPAddressField()
    domain_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.domain_name}"
    
class IPGeoLookup(models.Model):
    ip_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    isp = models.CharField(max_length=100, blank=True)
    raw_data = models.TextField(blank=True)  # Eklenen alan

    def __str__(self):
        return self.ip_address
