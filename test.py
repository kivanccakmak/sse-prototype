#!/bin/python3
import ast
import json
import requests

def main():
    """
    """
    token = login()
    # say_public_hello(token)
    say_auth_hello(token)

def say_public_hello(token):
    url = "http://127.0.0.1:5001/hello"
    data = {"key": "value"}
    headers = {}

    r = requests.post(url, json=data, headers=headers)
    output = r.json()

    print("status_code: {}".format(r.status_code))
    print("response-text: {}".format(output))

def say_auth_hello(token):
    url = "http://127.0.0.1:5001/auth_hello"
    data = {"key": "value"}
    headers = {'Authorization': 'Bearer {}'.format(token)}

    r = requests.post(url, json=data, headers=headers)
    output = r.json()

    print("status_code: {}".format(r.status_code))
    print("response-text: {}".format(output))

def login():
    """
    """
    url = "http://127.0.0.1:5001/rest/login"
    data = {"username": "kivanc", "password": "1234"}

    r = requests.post(url, json=data)
    output = r.json()

    return output["access_token"]

if __name__ == "__main__":
    main()
