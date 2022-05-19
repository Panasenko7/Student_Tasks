import requests

URL = 'https://catfact.ninja/fact'
response = requests.get(URL)
response_dict = response.json()
print(response_dict['fact'])