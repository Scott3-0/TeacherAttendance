import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import datetime
from random import randint

now = datetime.datetime.now()
curDate = now.day + now.month + now.year #equal to 9+17+2019=2045 on Sept 17, 2019
dayCode = curDate * (randint(1,99)) #Multiplies curDate by a random integer from 1 to 99

login = 'testertesting465@gmail.com'
password = ''
sender = 'testertesting465@gmail.com'
receivers = ['aidan.ksw@gmail.com']

print(dayCode)

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(receivers)
msg['Subject'] = "Test Message"

# Simple text message or HTML
TEXT = "Hello everyone,\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Important message.\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Thanks,\n"
TEXT = TEXT + "SMTP Robot"

msg.attach(MIMEText(TEXT))

filenames = []
for file in filenames:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, 'rb').read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                    % os.path.basename(file))
    msg.attach(part)

smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(sender, receivers, msg.as_string())

input()
