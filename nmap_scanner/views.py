import nmap
from django.shortcuts import render
from .models import NmapResult

def nmap_scan(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        nm = nmap.PortScanner()
        nm.scan(ip_address, ports='80-443', arguments='-T4')

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
                
        return render(request, 'scan_results.html', {'scan_result': scan_result})
    
    return render(request, 'index.html')