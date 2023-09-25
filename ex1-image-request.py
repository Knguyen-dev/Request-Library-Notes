'''

- Response object methods
.content: Content of the response in bytes; good for images and whatnot
.text: content of the response in unicode; good for giving the html markup for a page
.status_code: Returns the status code of the http code
    2. 200s: Success
    3. 300s: Redirects
    4. 400s: Client errors, trying to access a page that you odn't have permissions for. Basically 
        the issue lies on the client-side.
    5. 500s: Server errors, website isn't working properly or is down for some reason.
    NOTE: Mainly if we're monitoring a site for errors, we only care about client or server errors, while 
        the rest mean's we're ok. 

.ok: True if status code is less than 400.
.headers: Returns the header information of the repsonse object, which gives us a bunch of technical information about the response 
    object.

'''

import requests

imgURL = "https://imgs.xkcd.com/comics/python.png"

# Make a get request to an image url and receive a response object
response = requests.get(imgURL)

# Save that image by writing its image bytes (image data) to a file called "comic.png" 
with open("comic.png", "wb") as f:
    f.write(response.content)