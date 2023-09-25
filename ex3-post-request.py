'''
- Here's how a post request would be done to a server. 

- data: Represents typically form data, or some kind of data that we're sending or posting to a server.
'''

import requests
data = {
    "username": "John12",
    "password": "testing123",   
}
response = requests.post("https://httpbin.org/post", params=data)

# Returns json encoded content of a response.
print(response.json)