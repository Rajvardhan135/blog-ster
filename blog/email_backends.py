# import smtplib

# email = "rajvardhansinghchib@gmail.com"
# password = "qixyvyhtavstprdw"
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=email, password=password)
# connection.sendmail(email, "fjrnvnjjncjnfjnvj@gmail.com", msg='Hello')
# connection.close()

# email_backends.py
import smtplib

class EmailError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class SMTPEmailServer():
    def __init__(self, host, port):
        self.connection = None
        self.user = "rajvardhansinghchib@gmail.com"
        self.password = "qixyvyhtavstprdw"
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

# mail = CustomEmailBackend("smtp.gmail.com", 587)

# mail.send_mail('rajvardhansinghchib@gmail.com', ['rajvardhansinghchib@gmail.com'], "Mesaage from django server")
def send_mail(subject, sender, receipents, message):
        connection = None
        user = "rajvardhansinghchib@gmail.com"
        password = "qixyvyhtavstprdw"
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
        
'''
connection = None
        user = "rajvardhansinghchib@gmail.com"
        password = "qixyvyhtavstprdw"
        host = "smtp.gmail.com"
        port = 587
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receipents[0]
        msg['Subject'] = subject
        connection = smtplib.SMTP(host, port)
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(sender, receipents[0], msg=message)
'''