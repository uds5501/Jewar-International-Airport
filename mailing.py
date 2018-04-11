import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender='jewargnoida@gmail.com'

def email_OTP(mail,OTP):
    subject="Your OTP"
    message="Your requested OTP is: "+str(OTP)+" , note that it will be valid for only 5 minutes.Happy Journey!"
    
    username = 'jewargnoida'
    password ='jewar123noida'
    msg = MIMEMultipart()
    msg['From'] =sender
    msg['To'] = mail
    msg['Subject'] = 'Your OTP'
    msg.attach(MIMEText(message))
    server = smtplib.SMTP('smtp.googlemail.com')
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(username,password)
        server.sendmail(sender,mail,msg.as_string())
        print "\t\t\t\t\t\t\tYOUR OTP HAS BEEN SENT"
    except Exception:
        print "\t\t\t\t\t\t\tOOPS..some error occured durig ending your OTP"
    server.quit()

def email_Ticket(mail,Tick_info):
    a=Tick_info
    subject="Your Ticket"
    message="Your Ticket information is as follows: Ticket number: "+a[0]+" Name: "+a[1]+" Seat Number: "+a[3]+" Destination: "+a[4]+". Have a happy and safe journey!"
    
    username = 'jewargnoida'
    password ='jewar123noida'
    msg = MIMEMultipart()
    msg['From'] =sender
    msg['To'] = mail
    msg['Subject'] = 'Your Ticket'
    msg.attach(MIMEText(message))
    server = smtplib.SMTP('smtp.googlemail.com')
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(username,password)
        server.sendmail(sender,mail,msg.as_string())
        print "\t\t\t\t\t\tYOUR TICKET INFORMATION HAS BEEN SENT TO YOUR EMAiL ID"
    except Exception:
        print "\t\t\t\t\t\tOOPS..some error occured during sending your ticket information"
    server.quit()
    
    
