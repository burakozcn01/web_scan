from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web_tool import settings
import subprocess, nmap, requests

class NucleiToolAPIView(APIView):
    def post(self, request):
        target = request.data.get('target')
        cmd = [settings.NUCLEI_PATH, '-target', target, '-silent']
        result = subprocess.run(cmd, capture_output=True, text=True)

        return Response({'result': result.stdout, 'target': target}, status=status.HTTP_200_OK)


class NmapToolAPIView(APIView):
    def post(self, request):
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

        return Response({'ip_address': ip_address, 'scan_result': scan_result}, status=status.HTTP_200_OK)


class NiktoToolAPIView(APIView):
    def post(self, request):
        target = request.data.get('target')
        nikto_cmd = ['nikto', '-h', target]
        nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)

        return Response({'nikto_result': nikto_result.stdout, 'target': target}, status=status.HTTP_200_OK)


class ReverseIPDNSToolAPIView(APIView):
    def post(self, request):
        ip_address = request.data.get('ip_address')

        result = subprocess.run(['host', ip_address], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            domain_name = output.split(' ')[-1].strip()[:-1]

            return Response({'name_or_ip': domain_name}, status=status.HTTP_200_OK)
        else:
            return Response({'error_message': "Reverse IP-DNS sorgulaması başarısız oldu."}, status=status.HTTP_400_BAD_REQUEST)


class IPGeoLookupAPIView(APIView):
    def post(self, request):
        ip_address = request.data.get('ip_address')
        api_url = f'https://api.hackertarget.com/ipgeo/?q={ip_address}'

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.text.split('\n')
                city = data[0].split(':')[-1].strip()
                country = data[1].split(':')[-1].strip()
                state = data[2].split(':')[-1].strip()
                latitude = float(data[4].split(':')[-1].strip())
                longitude = float(data[5].split(':')[-1].strip())

                response_data = {
                    'City': city,
                    'Country': country,
                    'State': state,
                    'Latitude': latitude,
                    'Longitude': longitude,
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'error_message': "IP geolocation sorgulaması başarısız oldu."}, status=status.HTTP_400_BAD_REQUEST)

        except requests.exceptions.RequestException as e:
            return Response({'error_message': "IP geolocation API hatası."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)