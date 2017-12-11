import smtplib


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
email_conn.sendmail(from_header, to_list, "Hellow, test")
email_conn.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException 

naslidyvannja_classy = SMTP(host, port)
naslidyvannja_classy.ehlo()
naslidyvannja_classy.starttls()
try:
    naslidyvannja_classy.login(username, "Wrong Pass")
    naslidyvannja_classy.sendmail(from_header, to_list, "Hellow, test")
except SMTPAuthenticationError:
    print("SMTPAuthenticationError occured")
except:
    print("Some other error occured")
naslidyvannja_classy.quit()
