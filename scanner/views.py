import subprocess, nmap, nuclei
from django.shortcuts import render
from .models import NucleiScan
from .models import NmapResult
from .models import NiktoScan


def nuclei_scan(request): 
    if request.method == 'POST': # Eğer POST isteği ise
        target = request.POST.get('target') # Hedef URL'yi al
        cmd = ['/mnt/c/Users/BURAK/Desktop/web_scan/nuclei', '-target', target, '-silent'] # Nuclei komutunu oluştur
        result = subprocess.run(cmd, capture_output=True, text=True)  # Nuclei komutunu çalıştır

        # NucleiScan modelini kullanarak veritabanına kaydet
        nuclei_scan = NucleiScan(target=target, scan_output=result.stdout) 
        nuclei_scan.save() 

        return render(request, 'nuclei_scan_results.html', {'result': result.stdout, 'target': target}) # Sonuçları göster
    
    return render(request, 'nuclei.html') # Eğer POST isteği değilse index.html'i göster

def nmap_scan(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        nm = nmap.PortScanner()
        nm.scan(ip_address, ports='22,23,80,110,143,443,3389', arguments='-T4')

        scan_result = []
        for proto in nm[ip_address].all_protocols():
            lport = nm[ip_address][proto].keys()
            for port in lport:
                protocol = proto
                port_number = port
                state = nm[ip_address][proto][port]['state']
                service = nm[ip_address][proto][port]['name']
                scan_result.append((protocol, port_number, state, service))

                # Tarama sonuçlarını veritabanına kaydet
                nmap_result = NmapResult(ip_address=ip_address, port=port_number, protocol=protocol, state=state, service=service)
                nmap_result.save()
                
        return render(request, 'nmap_scan_results.html', {'scan_result': scan_result})
    
    return render(request, 'nmap.html')

def nikto_scan(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        nikto_cmd = ['nikto', '-h', target]
        nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)

        # Nikto tarama sonucunu veritabanına kaydet
        nikto_scan = NiktoScan(target=target, scan_output=nikto_result.stdout)
        nikto_scan.save()

        return render(request, 'nikto_scan_results.html', {'nikto_result': nikto_result.stdout, 'target': target})

    return render(request, 'nikto.html')

def reverse_ip_lookup(request):
    if request.method == 'POST':
        ip_address = request.POST['ip_address']

        # Terminal komutunu çalıştırın ve çıktıyı alın
        result = subprocess.run(['host', ip_address], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            domain_name = output.split(' ')[-1].strip()[:-1]  # Alan adını çıkartın
            return render(request, 'reverse_ip_result.html', {'domain_name': domain_name})
        else:
            error_message = "Reverse IP-DNS sorgulaması başarısız oldu."
            return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'reverse_ip_lookup.html')