#!?usr/bin/env python 
# 
# HTML and multimedia content in email
# 
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

sender = 'sender_emailid'
password = getpass.getpass()
receiver = 'receiver_emailid'

text = MIMEMultipart()
text['Subject'] = 'Test HTML Content'
text['From'] = sender
text['To'] = receiver

msg = """\
<html>
  <body>
    <p>Hello there, <br>
       Good day !!<br>
       <a href="http://www.imdb.com">Home</a>
    </p>
  </body>
</html>
"""

html_content = MIMEText(msg, "html")
text.attach(html_content)
s = smtplib.SMTP_SSL(host_name, port)
print("Mail sent successfully !!")

s.login(sender, password)
s.sendmail(sender, receiver, text.as_string())
s.quit()

