import subprocess
import nmap
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NucleiScan, NmapResult, NiktoScan, ReverseIPLookupResult


def index(request):
    return render(request, 'index.html')


def nuclei_tool(request): 
    if request.method == 'POST':
        target = request.POST.get('target')
        cmd = ['/mnt/c/Users/BURAK/Desktop/web_scan/nuclei', '-target', target, '-silent']
        result = subprocess.run(cmd, capture_output=True, text=True)

        nuclei_scan = NucleiScan(target=target, scan_output=result.stdout)
        nuclei_scan.save()

        return render(request, 'nuclei_scan_results.html', {'result': result.stdout, 'target': target})
    
    return render(request, 'nuclei.html')


def nmap_tool(request):
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

                # Veritabanında aynı IP adresine ait kayıt varsa güncelle, yoksa oluştur
                nmap_result, created = NmapResult.objects.update_or_create(
                    ip_address=ip_address,
                    port=port_number,
                    protocol=protocol,
                    defaults={'state': state, 'service': service}
                )

        return render(request, 'nmap_scan_results.html', {'scan_result': scan_result})
    
    return render(request, 'nmap.html')


def nikto_tool(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        nikto_cmd = ['nikto', '-h', target]
        nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)

        nikto_scan = NiktoScan(target=target, scan_output=nikto_result.stdout)
        nikto_scan.save()

        return render(request, 'nikto_scan_results.html', {'nikto_result': nikto_result.stdout, 'target': target})

    return render(request, 'nikto.html')


def reverse_ip_dns_tool(request):
    if request.method == 'POST':
        ip_address = request.POST['ip_address']

        result = subprocess.run(['host', ip_address], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            domain_name = output.split(' ')[-1].strip()[:-1]

            # Veritabanında aynı IP adresine ait kayıt varsa güncelle, yoksa oluştur
            reverse_ip_result, created = ReverseIPLookupResult.objects.update_or_create(
                ip_address=ip_address,
                defaults={'domain_name': domain_name}
            )

            return render(request, 'reverse_ip_result.html', {'domain_name': domain_name})
        else:
            error_message = "Reverse IP-DNS sorgulaması başarısız oldu."
            return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'reverse_ip_lookup.html')


@api_view(['POST'])
def nuclei_tool_api(request): 
    if request.method == 'POST':
        target = request.data.get('target')
        cmd = ['/mnt/c/Users/BURAK/Desktop/web_scan/nuclei', '-target', target, '-silent']
        result = subprocess.run(cmd, capture_output=True, text=True)

        nuclei_scan = NucleiScan(target=target, scan_output=result.stdout)
        nuclei_scan.save()

        return Response({'result': result.stdout, 'target': target}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def nmap_tool_api(request):
    if request.method == 'POST':
        ip_address = request.data.get('ip_address')
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
                scan_result.append({'protocol': protocol, 'port_number': port_number, 'state': state, 'service': service})

                # Veritabanında aynı IP adresine ait kayıt varsa güncelle, yoksa oluştur
                nmap_result, created = NmapResult.objects.update_or_create(
                    ip_address=ip_address,
                    port=port_number,
                    protocol=protocol,
                    defaults={'state': state, 'service': service}
                )

        return Response({'ip_address': ip_address, 'scan_result': scan_result}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def nikto_tool_api(request):
    if request.method == 'POST':
        target = request.data.get('target')
        nikto_cmd = ['nikto', '-h', target]
        nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)

        nikto_scan = NiktoScan(target=target, scan_output=nikto_result.stdout)
        nikto_scan.save()

        return Response({'nikto_result': nikto_result.stdout, 'target': target}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reverse_ip_dns_tool_api(request):
    if request.method == 'POST':
        ip_address = request.data.get('ip_address')

        result = subprocess.run(['host', ip_address], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            domain_name = output.split(' ')[-1].strip()[:-1]

            # Veritabanında aynı IP adresine ait kayıt varsa güncelle, yoksa oluştur
            reverse_ip_result, created = ReverseIPLookupResult.objects.update_or_create(
                ip_address=ip_address,
                defaults={'domain_name': domain_name}
            )

            return Response({'domain_name': domain_name}, status=status.HTTP_200_OK)
        else:
            return Response({'error_message': "Reverse IP-DNS sorgulaması başarısız oldu."}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)
