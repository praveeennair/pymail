import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Praveen'
email['to'] = 'textpraveennair@gmail.com'
email['subject'] = 'Hey Python first Mail'

email.set_content(html.substitute(name='Praveen'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('praveen.lassopic@gmail.com', '($#Praveen)')
    smtp.send_message(email)
    print('all good')
    