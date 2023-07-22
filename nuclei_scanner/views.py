import subprocess
from django.shortcuts import render
from .models import NucleiScan

def nuclei_scan(request): 
    if request.method == 'POST': # Eğer POST isteği ise
        target = request.POST.get('target') # Hedef URL'yi al
        cmd = ['/usr/bin/nuclei', '-target', target, '-silent'] # Nuclei komutunu oluştur
        result = subprocess.run(cmd, capture_output=True, text=True)  # Nuclei komutunu çalıştır

        # NucleiScan modelini kullanarak veritabanına kaydet
        nuclei_scan = NucleiScan(target=target, scan_output=result.stdout) 
        nuclei_scan.save() 

        return render(request, 'nuclei_scan_results.html', {'result': result.stdout, 'target': target}) # Sonuçları göster
    
    return render(request, 'nuclei.html') # Eğer POST isteği değilse index.html'i göster