'''
- Assume the username is 'John12' and 'testing123' was the password to their account. Below is an example on how authentication
    could work

'''
import requests
credentials = (
    "John12",
    "testing123",   
)
response = requests.get("https://httpbin.org/basic-auth/John12/testing123", auth=credentials)

print(response)