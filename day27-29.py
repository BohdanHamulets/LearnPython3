import requests
from twilio.rest import Client
#username= "chillimilli"
#password = "SuperGoodPassword"
account_sid = ""
auth_token = ""


#twilio_phone = ''
#my_phone = ""
#maria_phone = ""

base_url = 'https://api.twilio.com/2010-04-01'
message_url = base_url + "/Accounts/" + account_sid + "Messages/"

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

client = Client(account_sid, auth_token)

#auth = (account_sid, auth_token)
r = requests.post(message_url, auth=auth)

i = 0
img = "http://travel.home.sndimg.com/content/dam/images/travel/fullset/2016/03/07/california-beach-getaway-pismo-beach.jpg.rend.hgtvcom.966.725.suffix/1491592782974.jpeg"

while i < 10:
    smska = "Spam number {number}".format(number=i)
    message_data = client.messages.create(
            my_phone,
            body="",
            from_=twilio_phone,
            media_url=img
            )
    i += 1

print(message_data.sid)

r = requests.post(message_url, data=message_data, auth=auth)

print(r.text)
xml_pretty(r.text)