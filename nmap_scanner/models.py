from django.db import models

class NmapResult(models.Model):
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    service = models.CharField(max_length=100)

   
    class meta:
        ordering = ['-created_at']
        db_table = 'nmap_scan'
        verbose_name = 'nmap taraması'
        verbose_name_plural = 'nmap taramaları'


    def __str__(self):
        return f"{self.ip_address}:{self.port}"