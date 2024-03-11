# import smtplib

# email_backends.py
import smtplib
from django.conf import settings

class EmailError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class SMTPEmailServer():
    def __init__(self, host, port):
        self.connection = None
        self.user = settings.EMAIL_HOST_USER
        self.password = settings.PASSWORD
        self.host = host
        self.port = port
    
    def send_mail(self, sender, receipents, message):
        try:
            self.connection = smtplib.SMTP(self.host, self.port)
            self.connection.starttls()
            self.connection.login(user=self.user, password=self.password)
            for receipent in receipents:
                self.connection.sendmail(sender, receipent, msg=message)

            self.connection.close()
        except(smtplib.SMTPRecipientsRefused):
            raise EmailError("Invalid email provided")


def send_mail(subject, sender, receipents, message):
        connection = None
        user = settings.EMAIL_HOST_USER
        password = settings.PASSWORD
        host = "smtp.gmail.com"
        port = 587
        message = 'Subject: {}\n\n{}'.format(subject, message)
        try:
            connection = smtplib.SMTP(host, port)
            connection.starttls()
            connection.login(user=user, password=password)
            for receipent in receipents:
                connection.sendmail(sender, receipent, msg=message)
            connection.close()
        except(smtplib.SMTPRecipientsRefused):
            raise EmailError("Invalid email provided")
