#!/bin/python3
import json
import requests

def main():
    """
    """
    url = "http://127.0.0.1:5001/hello"
    data = {"key": "value"}
    r = requests.post(url, json=data)

    print("status_code: {}".format(r.status_code))
    print("response-text: {}".format(r.json()))

if __name__ == "__main__":
    main()
