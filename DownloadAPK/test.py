import requests

url = 'https://d.apkpure.com/b/XAPK/uni.UNI683BE87?version=latest'
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.apkpure.com/'
}
timeout = 10

response = requests.get(url, headers=headers, timeout=timeout, stream=True)

for header, value in response.headers.items():
    print(f"{header}: {value}")