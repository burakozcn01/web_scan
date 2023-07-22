import nmap
from django.shortcuts import render

def nmap_scan(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        nm = nmap.PortScanner()
        nm.scan(ip_address, ports='1-100', arguments='-T5')

        scan_result = []
        for proto in nm[ip_address].all_protocols():
            lport = nm[ip_address][proto].keys()
            for port in lport:
                scan_result.append(
                    (proto, port, nm[ip_address][proto][port]['state'], nm[ip_address][proto][port]['name']))
                
        return render(request, 'scan_results.html', {'scan_result': scan_result})
    return render(request, 'index.html')