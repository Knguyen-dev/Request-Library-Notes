'''

- httpbin.org: Basically a website where we can test the requests library. Has different urls for testing something so a url for testing get requests,
    authentication, etc.

- Below is an example on how we can pass query parameters into an http request. For example, 'https://someWebsite.com/items?cost=10&color=blue' etc.

'''

import requests

# Create dictionary that contains query parameter keys and their values
payload = {
    "page": 2,
    "count": 25,
}

# Then doing response1.text would give us the json for the response object, allowing us to verify whether 
# our get request to http bin was correct
response = requests.get("https://httpbin.org/get", params=payload)