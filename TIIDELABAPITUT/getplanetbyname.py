import requests

BASE_URL = 'https://swapi.dev/api/'


headers = {
    "Content-type": "Application/json"
    # "Authentication" : ""
}

planets_endpoint = BASE_URL + 'planets' #gets all planets

response = requests.get(planets_endpoint,headers=headers)
number_of_data = response.json()['count']
print(number_of_data)
