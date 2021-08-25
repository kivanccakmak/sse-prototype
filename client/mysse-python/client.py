import json
import pprint
import requests
import sseclient # sseclient-py

def login():
    """
    """
    url = "http://127.0.0.1:5001/rest/login"
    data = {"username": "kivanc", "password": "1234"}

    r = requests.post(url, json=data)
    output = r.json()

    return output["access_token"]

url = 'http://127.0.0.1:5001/stream'
token = login()
headers = {'token': token}

print("creating stream response")
stream_response = requests.get(url, headers=headers, stream=True)

print("creating client")
client = sseclient.SSEClient(stream_response)

print("loop")
# Loop forever (while connection "open")
for event in client.events():
    print ("got a new event from server")
    pprint.pprint(event.data)
