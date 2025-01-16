"""Main module."""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailNotifications():

    RECIPIENTS = None
    CC_EMAIL = None
    BCC_EMAIL =  None

    def __init__(self, from_email:str, to_email:list, password:str, 
                 message:str, subject: str=None, 
                 smtp_server:str = "smtp.gmail.com",
                 smtp_port:int = 465):
        self.__from_email = from_email
        self.__to_email = to_email
        self.__password = password
        self.__message = message
        self.__subject = subject

        self.__smtp_server = smtp_server
        self.__smtp_port = smtp_port
    
    def send_email_smtp_ssl(self):
        msg = MIMEMultipart()
        msg['From'] = self.__from_email
        msg['To'] = ",".join(self.__to_email)
        msg['Subject'] = self.__subject

        body = f"""
                {self.__message}
                """
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL(self.__smtp_server, self.__smtp_port) as server:
            server.login(self.__from_email, self.__password)
            server.sendmail(self.__from_email, self.__to_email, msg.as_string())
    
    def send_email_smtp_tls(self):
        msg = MIMEMultipart()
        msg['From'] = self.__from_email
        msg['To'] = ",".join(self.__to_email)
        msg['Subject'] = self.__subject

        body = f"""
                {self.__message}
                """
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL(self.__smtp_server, self.__smtp_port) as server:
            server.starttls()
            server.login(self.__from_email, self.__password)
            server.sendmail(self.__from_email, self.__to_email, msg.as_string())