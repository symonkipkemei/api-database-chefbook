'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''


import requests
from pprint import pprint

base_url = "https://restcountries.com/v3.1/name/kenya"


response = requests.get(base_url)

print(f"Status code: {response.status_code}")
print()
pprint(f"Headers:  {response.headers}")
print()
pprint(response.json())