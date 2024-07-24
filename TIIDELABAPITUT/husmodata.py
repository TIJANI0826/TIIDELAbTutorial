import requests
import json
import os
from getplanid import getplanid
BASE_URL = "https://www.husmodata.com/api/"

token = os.getenv("HUSMODATA_TOKEN") #get token value form the environment

# headers = {
#     "Authorization" : "Token {}".format(token),
#     "Content-Type" : "application/json"
# }

# authorization_token = requests.get(BASE_URL,headers=headers)
# print(authorization_token)

# def getplanid(network_id,size ):
    
#     if network_id == 1:
#         if size == "15":
#             return 13
#         elif size == "11":
#             return 14
#     elif network_id == 2:
#         if size == "18":
#             return 27


def buydata():
    
    url = "https://www.husmodata.com/api/data/"

    network = int(input("input the network e,g \n Type 1 for MTN, 2 for Glo, 3 for Airtel, 4 for 9Mobile: "))
    mobile_number = input("Input your mobile number: ")
    data_size = input("How many gig do you want to buy e.g 2 for 2 GB etc: ")


    payload = json.dumps({
        "network": network,
        "mobile_number": mobile_number,
        "plan": getplanid(network,data_size), 
        "Ported_number": True
    })
    
    headers = {
    'Authorization': 'Token {}'.format(token),
    'Content-Type': 'application/json'
    }

    # response = requests.request("POST",url headers=headers,data=payload)
    response = requests.post(url, headers=headers, data=payload)

    print(response.json())

buydata()