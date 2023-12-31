import requests

url = 'http://127.0.0.1:8000/nmap-api/'  
ip_address = '192.30.255.112' 

payload = {'ip_address': ip_address}
response = requests.post(url, data=payload)

if response.status_code == 200:
    data = response.json()
    print("Nmap Sonuçları:")
    for scan_result in data['scan_result']:
        print("Protocol:", scan_result['protocol'])
        print("Port Number:", scan_result['port_number'])
        print("State:", scan_result['state'])
        print("Service:", scan_result['service'])
        print("------------")
else:
    print("Hata Kodu:", response.status_code)
    print("Hata Mesajı:", response.text)
