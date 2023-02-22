import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



smtp_server ="" #the smtp server for your email  eg for gmail it's smtp.gmail.com
port_number = int() # the port to use
sender_adddress =""  
sender_password ="" #password to the email address for authentication purposes..for gmail create an app password instead 
receiver_address = ""


server = smtplib.SMTP(smtp_server, port_number)

server.ehlo()
server.login(sender_adddress, sender_password)

msg = MIMEMultipart()
msg['From'] = 'Xxxxx Xxxxx'
msg['To'] = receiver_address
msg['Subject'] = 'Just Testing My Python Skills'

#reading the body of the message from body.txt 
with open('body.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))  # attaching the message to the msg as plain text

# initializing an image file to attach to the email
filename = 'mywork.png' 
attachment = open(filename, 'rb')     

#creating a payload for attachments
p = MIMEBase('application', 'octet-stream') 
p.set_payload(attachment.read()) 

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p) # attaching the payload to the email

text = msg.as_string()
server.sendmail(sender_adddress,receiver_address,text)