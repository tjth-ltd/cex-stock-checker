import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
name = sys.argv[1]
id = sys.argv[2] 
mail_content = '''Hello,

Your item is in stock on CEX!

Item: ''' +str(name) + '''
URL: https://uk.webuy.com/product-detail?id=''' +str(id) + '''

You're welcome,

CEX Stock Checker
CEX Stock Checker designed and created by TJTH Ltd https://tjth.co
'''
#The mail addresses and password
sender_address = 'SMTP_LOGIN'
sender_pass = 'YOUR_PASSWORD'
receiver_address = 'RECIPIENT_ADDRESS'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'CEX Stock Checker - Item in Stock'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('SMTP_SERVER_ADDRESS', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent to ' + str(receiver_address))