#!/usr/bin/python3
'''
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    data = response.json()
    print(data.get("id"))
