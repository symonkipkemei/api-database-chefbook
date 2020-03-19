'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''