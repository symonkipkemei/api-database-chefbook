'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''


import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"


file = {
    "first_name" : "symon",
    "last_name":"kipchumba",
    "email":"kipchumba@codingnomads.co"
}

post = requests.post(base_url,json=file)

# verify if message has been post

response = requests.get(base_url)


pprint(f"STATUS CODE : {response.status_code}")
pprint(f"ENCODING : {response.encoding}")
pprint(f"RESPONSE BODY : {response.json()}")

