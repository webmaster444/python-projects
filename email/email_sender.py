import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Andrei'
email['to'] = 'yikiw15201@mijumail.com'
email['subject'] = 'you won $'
email.set_content(html.substitute(name="Bob"), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('devwork8888@gmail.com', 'eoqldir111')
    smtp.send_message(email)
    print('all good')
