'''
Create a Slack API token for the codingnomads workspace.

Using the slackclient package or the requests package, fetch all comments that include links
from the python-resources channel.

Create a list of dictionaries with the following format:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

Next, create the necessary tables in a database to model this data.

Think about what tables are required to model this object. Do you need two tables? Three?

Now, persist the data that you retrieve using the Slack API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''