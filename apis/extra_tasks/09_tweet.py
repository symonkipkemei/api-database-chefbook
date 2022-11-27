'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''


from requests_oauthlib import OAuth1Session
import os
import json
import requests
import time
import datetime

# keys 
consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")



def authorization_process():
       # Get request_token
       request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
       oauth = OAuth1Session(consumer_key,client_secret=consumer_secret)


       try:
              fetch_response = oauth.fetch_request_token(request_token_url)
              print(fetch_response)
              print("It worked!")
       except ValueError:
              print( "There might be an issue with one of your keys")

       resource_owner_key = fetch_response["oauth_token"]
       resource_owner_secret = fetch_response["oauth_token_secret"]

       print(f"Got OAuth token: {resource_owner_key}")



       # Get authorization
       base_authorization_url = "https://api.twitter.com/oauth/authorize"
       authorization_url = oauth.authorization_url(base_authorization_url)
       print(f"Please go here and authorize: {authorization_url}")
       verifier = input("Paste the PIN here: ")


       # Get access token
       access_token_url = "https://api.twitter.com/oauth/access_token"
       oauth = OAuth1Session(
           consumer_key,
           client_secret=consumer_secret,
           resource_owner_key=resource_owner_key,
           resource_owner_secret=resource_owner_secret,
           verifier=verifier,
       )

       oauth_tokens = oauth.fetch_access_token(access_token_url)

       access_token = oauth_tokens["oauth_token"]
       access_token_secret = oauth_tokens["oauth_token_secret"]

       print(oauth)

       return oauth


# authentication from tweeter to read, write and post

payload1 = {"text": f"Hello world! Check your clock, it's {datetime.datetime.now()}"}
payload2 = {"text": f"Hello world! Check your clock, it's {datetime.datetime.now()}"}


def tweet(oauth, payload):
       # make the request
       response = oauth.post(
              "https://api.twitter.com/2/tweets",
              json=payload,
          )

       if response.status_code != 201:
           raise Exception(
               f"Request returned an error: {response.status_code} {response.text}"
           )


       print(f"Response code: {response.status_code}")

       # Saving the response as JSON
       json_response = response.json()
       print(json.dumps(json_response, indent=4, sort_keys=True))

def main():
       # get authorization
       oauth = authorization_process()

       while True:
              tweet(oauth,payload1)
              time.sleep(3)


main()            