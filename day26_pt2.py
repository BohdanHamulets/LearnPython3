import json
import requests
from requests_oauthlib import OAuth2



client_id = "0p3nQve_S9RGarSa61LZgw"
client_secret = "5kDllAvYay4AEoDr02dHXf7TXapNEt8JqL2nR9KBlFP03HRNjgpVp4wmHFWp0uVM"
#token is modified on purpose so don't try to use it - it will not work anyway
token = {
    "access_token": "Zb7pq2WeAsGLAwArbXsSqYK1jhJoUtfJ8Ok2SDSpD0k144QKEWq04KNKzBdeTCOkxeRHES12h4_h-EdIg8M5WUyXCyY-67M-DhvPpLta9j8kikNZXcqPBMtOYXUlWnYx",
    "expires_in": 635002403,
    "token_type": "Bearer"
}


#tried to get OAuth2 to work, but as in the traning material only 1st versiob is available,
#I can't be waisting to much time as I don't work closely with API
#need to get my prioroties straight :)

r = oauth.get("https://api.yelp.com/v3/businesses/search?term=food,location='San+Francisco'")

base_url ="https://api.yelp.com/v3/businesses/search?term=food,location='San+Francisco'"
auth = OAuth2(client_id, client_secret, token)
search_body = {}
url = "{base_url}?term={term}, location={location}".format(base_url=base_url, 
    term=food, 
    location='San+Francisco')
r = requests.post(url, headers=None, body= auth=auth)



"""def __init__(self, client_id=None, client=None, auto_refresh_url=None,
            auto_refresh_kwargs=None, scope=None, redirect_uri=None, token=None,
            state=None, token_updater=None, **kwargs):
"""

