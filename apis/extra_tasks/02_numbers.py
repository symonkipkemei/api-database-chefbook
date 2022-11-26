'''
Create an API that serves numerical information.

What topic your API is about is your own choice,
however it needs to fulfill the following specs:
* ingest API data from at least 1 external source
* combine (and/or manipulate) the received data in a meaningful way
* store your altered data in a Postgres database
* serve the data at an endpoint (e.g. using sandman2)

TIP: consider using a cryptocurrency API such as coinmarketcap (but anything goes)!

'''

import os
import requests
from pprint import pprint


coinmarketcap_api_key = os.environ["coinmarketcap_api_key"]

print(coinmarketcap_api_key)