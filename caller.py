import requests

URL = "http://localhost:8000/filter/"
PARAMS = {'species':'dog', 'gender': 'male', 'personality': 'lazy'}
response = requests.get(url = URL, params = PARAMS)

data = response.json()
print(data)
