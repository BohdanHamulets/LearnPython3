import requests
from twilio.rest import Client
#username= "chillimilli"
#password = "SuperGoodPassword"
account_sid = "AC1ec4fa564de794d593b27b04fbde8882"
auth_token = "a7017b26653f62eb0b19e52f695fa282"


twilio_phone = '+13126545077'
my_phone = "+380937088188"
maria_phone = "+380937087088"

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


message_data = client.messages.create(
        maria_phone,
        body="Hi, newbie ^_^",
        from_=twilio_phone,
        )

print(message_data.sid)

r = requests.post(message_url, data=message_data, auth=auth)

print(r.text)
xml_pretty(r.text)