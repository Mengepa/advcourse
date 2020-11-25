import requests

url = 'https://www.google.com'
r = requests.get(url)
response = requests.get(url)
print(f'Response returned: {response.status_code}, {response.reason}')
print(response.text)