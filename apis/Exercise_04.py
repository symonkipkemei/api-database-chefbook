'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''


import requests
from pprint import pprint


base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body= {
    "email":"symonkipkemei@codingnomass.co",
    "first_name" : "mandich",
    "last_name":"lawi"
}

response = requests.put(base_url + "/342" , json=body)

pprint(f"response code : {response.status_code}")

