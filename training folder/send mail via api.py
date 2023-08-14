# import requests


# def send_simple_message():
#     return requests.post(
#         "https://api.mailgun.net/v3/sandboxf9be6b10162d442d97efadbc134ecb04.mailgun.org/messages",
#         auth=("api", "0913e665871018d0accf8a564bfe72e7-28e9457d-c7122ac6"),
#         data={"from": "Mailgun Sandbox <postmaster@sandboxf9be6b10162d442d97efadbc134ecb04.mailgun.org>",
#               "to": "Amin Soltani <aminsoltani.1221@gmail.com>",
#               "subject": "Hello Amin Soltani",
#               "text": "Congratulations Amin Soltani, you just sent an email with Mailgun!  You are truly awesome!"})

# send_simple_message()
import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "aminsoltani.1221@gmail.com"
recipients = ["aminsoltani.137979@gmail.com"]
password = "Hossain110@"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = "aminsoltani.137979@gmail.com"
    with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)