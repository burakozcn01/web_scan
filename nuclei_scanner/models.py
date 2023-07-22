from django.db import models

class NucleiScan(models.Model):
    target = models.CharField(max_length=100) 
    scan_output = models.TextField()

    def __str__(self):
        return self.target
