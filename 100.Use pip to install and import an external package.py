#100.Use pip to install and import an external package
import requests
response=requests.get('https://api.github.com')
print("Status Code:", response.status_code)
