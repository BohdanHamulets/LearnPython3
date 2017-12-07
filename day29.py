import twitter

Consumer_Key = '' # (API Key)
Consumer_Secret = '' #(API Secret)
#Access Level    Read and write (modify app permissions)
Owner = ''
Owner_ID = ''


Access_Token = ""
Access_Token_Secret = ""

#Notice that I've hide my credentials for security reasons (more evem common sense reasons :)

api = twitter.Api(
    consumer_key = Consumer_Key,
    consumer_secret=Consumer_Secret,
    access_token_key= Access_Token,
    access_token_secret=Access_Token_Secret)

print(api.VerifyCredentials())

followers = api.GetFollowers()
friends = api.GetFriends()

tweet = api.PostUpdates(status="Thanks @justinmitchel #Python3 is amazing! #30daysofpython")