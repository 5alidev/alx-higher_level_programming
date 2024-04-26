#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
    except requests.HTTPError as e:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
