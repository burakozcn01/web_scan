from django.db import models

class NiktoScan(models.Model):
    target = models.CharField(max_length=255)
    scan_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nikto Scan for {self.target} at {self.created_at}"
