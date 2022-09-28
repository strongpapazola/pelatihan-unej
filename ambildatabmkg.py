import requests

url = 'https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json'
result = requests.get(url).json()['Infogempa']['gempa']
print(result['Coordinates'])
print(result['Tanggal'])
print(f"https://data.bmkg.go.id/DataMKG/TEWS/{result['Shakemap']}")



