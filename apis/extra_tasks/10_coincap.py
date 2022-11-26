'''
Sign up for an API key with the coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''



import os
import requests
from pprint import pprint


coinmarketcap_api_key = os.environ["coinmarketcap_api_key"]


base_url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency"

historical_listing = "/listings/latest"

endpoint = base_url + historical_listing
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coinmarketcap_api_key,
}


response = requests.get(endpoint,headers=headers)

print(response.status_code)
pprint(response.headers)

feedback = response.json()


for data in feedback["data"]:
    print(data["cmc_rank"])
