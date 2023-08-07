from web_tool import settings
from django.http import HttpResponse
import requests, subprocess, nmap
from scanner.models import NucleiScan, NmapResult, NiktoScan, ReverseIPLookupResult, IPGeoLookup


class NucleiTool:
    def __init__(self, target):
        self.target = target

    def scan(self):
        cmd = [settings.NUCLEI_PATH, '-target', self.target, '-silent']
        result = subprocess.run(cmd, capture_output=True, text=True)

        nuclei_result, created = NucleiScan.objects.update_or_create(
            target=self.target,
            defaults={'scan_output': result.stdout}
        )

        return result.stdout
    
    def get_scan_results(self):
        return NucleiScan.objects.filter(target=self.target)
    
class NiktoTool:
    def __init__(self, target):
        self.target = target

    def scan(self):
        nikto_cmd = ['nikto', '-h', self.target]
        result = subprocess.run(nikto_cmd, capture_output=True, text=True)
        
        nikto_result, created = NiktoScan.objects.update_or_create(
            target=self.target,
            defaults={'scan_output': result.stdout}
        )

        return result.stdout
    
    def get_scan_results(self):
        return NiktoScan.objects.filter(target=self.target)
    

class NmapTool:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def scan(self):
        nm = nmap.PortScanner()
        nm.scan(self.ip_address, ports='22,23,80,110,143,443,3389', arguments='-T4')

        scan_result = []
        for proto in nm[self.ip_address].all_protocols():
            lport = nm[self.ip_address][proto].keys()
            for port in lport:
                protocol = proto
                port_number = port
                state = nm[self.ip_address][proto][port]['state']
                service = nm[self.ip_address][proto][port]['name']
                scan_result.append((protocol, port_number, state, service))

                nmap_result, created = NmapResult.objects.update_or_create(
                    ip_address=self.ip_address,
                    port=port_number,
                    protocol=protocol,
                    defaults={'state': state, 'service': service}
                )

        return scan_result
    
    def get_scan_results(self):
        return NmapResult.objects.filter(ip_address=self.ip_address)
    

class ReverseIPLookup:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def lookup(self):
        result = subprocess.run(['host', self.ip_address], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            domain_name = output.split(' ')[-1].strip()[:-1]

            reverse_ip_result, created = ReverseIPLookupResult.objects.update_or_create(
                ip_address=self.ip_address,
                defaults={'domain_name': domain_name}
            )

            return domain_name
        else:
            return None
        
class IPGeoLookup:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def lookup(self):
        url = f"https://api.hackertarget.com/ipgeo/?q={self.ip_address}"
        try:
            response = requests.get(url)
            data = response.text.split('\n')
            city = data[0].split(':')[-1].strip()
            country = data[1].split(':')[-1].strip()
            state = data[2].split(':')[-1].strip()
            latitude = float(data[4].split(':')[-1].strip())
            longitude = float(data[5].split(':')[-1].strip())

            ip_geo_data, _ = IPGeoLookup.objects.update_or_create(
                ip_address=self.ip_address,
                defaults={
                    'country': country,
                    'state': state,
                    'city': city,
                    'latitude': latitude,
                    'longitude': longitude,
                }
            )
            return ip_geo_data

        except Exception as e:
            return None
