'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)
message = response.json()


for  key, value in message.items():
    for val in value:
        print(val["email"])

