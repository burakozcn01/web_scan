from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .service import NucleiTool, NiktoTool, NmapTool, ReverseIPLookup, IPGeoLookup, SslyzeTool
import subprocess , requests

def index(request):
    return render(request, 'index.html')

def nuclei_tool(request): 
    if request.method == 'POST':
        target = request.POST.get('target')
        nuclei = NucleiTool(target)
        result = nuclei.scan()
        return render(request, 'nuclei_scan_results.html', {'result': result, 'target': target})
    
    return render(request, 'nuclei.html')

def nmap_tool(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        nmap_tool = NmapTool(ip_address)
        scan_result = nmap_tool.scan()
        return render(request, 'nmap_scan_results.html', {'scan_result': scan_result})
    
    return render(request, 'nmap.html')

def nikto_tool(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        nikto = NiktoTool(target)
        nikto_result = nikto.scan()
        return render(request, 'nikto_scan_results.html', {'nikto_result': nikto_result, 'target': target})

    return render(request, 'nikto.html')

def reverse_ip_dns_tool(request):
    if request.method == 'POST':
        ip_address = request.POST['ip_address']
        reverse_ip_tool = ReverseIPLookup(ip_address)
        domain_name = reverse_ip_tool.lookup()
        
        if domain_name:
            return render(request, 'reverse_ip_result.html', {'domain_name': domain_name})
        else:
            error_message = "Reverse IP-DNS sorgulaması başarısız oldu."
            return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'reverse_ip_lookup.html')

def ip_geo_lookup(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        ip_geo_tool = IPGeoLookup(ip_address)
        ip_geo_data = ip_geo_tool.lookup()

        return render(request, 'ip_geo_lookup.html', {'ip_geo_data': ip_geo_data})

    return render(request, 'ip_geo_lookup.html')

def sslyze_tool(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        sslyze = SslyzeTool(target)
        sslyze_result = sslyze.scan()
        return render(request, 'sslyze_scan_results.html', {'sslyze_result': sslyze_result, 'target': target})

    return render(request, 'sslyze.html')