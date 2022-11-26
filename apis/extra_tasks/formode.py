
import os
import requests
from pprint import pprint



base_url = "https://formode.ke/portfolio"


response = requests.get(base_url)

print(response.status_code)
print(response.headers)

print(response.text)