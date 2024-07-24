import requests
import pprint
#Calling an API

    
BASE_URL = 'https://swapi.dev/api/'

# POST submitting, inserting, creating, GET/ receive data ,
# UPDATE/modifying data, AND PUT
headers = {
    "Content-type": "Application/json"
}
#collect the planet number to get informatio about a particular planet
id = input("type your planet id: ") 
#Starwars Planet 
planets = BASE_URL + 'planets/' # get all planets information endpoint
planets = BASE_URL + 'planets/' + id #get planet by its id number endpoint
response = requests.get(planets, headers=headers) # calling the API, getting all planets information
response_result = response.json() 
# print(response_result) #succesful 200, 201 post request, problem with your 404
# print()
# print(len(response_result))
# for i in response_result:
#     print(i)
#     print()

pprint.pprint(response_result)