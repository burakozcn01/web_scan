import subprocess
from django.shortcuts import render
from .models import NiktoScan

def nuclei_scan(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        nikto_cmd = ['nikto', '-h', target]
        nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)

        # Nikto tarama sonucunu veritabanına kaydet
        nikto_scan = NiktoScan(target=target, scan_output=nikto_result.stdout)
        nikto_scan.save()

        return render(request, 'nikto_scan_results.html', {'nikto_result': nikto_result.stdout, 'target': target})

    return render(request, 'index.html')
