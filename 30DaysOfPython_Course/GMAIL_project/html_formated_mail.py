import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



host = "smtp.gmail.com"
port = 587
username = "chilli"
password = 
from_header = "chilli"
to_list = ["chilli"]


email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
try:
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello, there"
    the_msg["From"] = from_header
    the_msg["To"] = to_list[0]
    plain_txt = "This is a body of the message"
    html_txt= """\
    <html>
        <head></head>
        <body>
            <p>Hey! I just met you, and zis is crazy!<br>
            But here's my number <b>380937088188</b>.
            Made by <a href='http://google.com'>GOOGLE</a>.
            </p>
        </body>
    </html>
    """
    part1 = MIMEText(plain_txt, 'plain')
    part2 = MIMEText(html_txt, "html")
    the_msg.attach(part1)
    the_msg.attach(part2)
    email_conn.sendmail(from_header, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPAuthenticationError:
    print("SMTPAuthenticationError occured")
except:
    print("Some other error occured")
