import requests
import json
def send_message(email,first_name,last_name,message):
    url = "https://tjib26.pythonanywhere.com/api/send-message/"
    payload = json.dumps({
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "message": message
        })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #return response.text

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response}")

send_message("tijanibrahim24@gmail.com","Ibrahim","Tijani","Test Passed")