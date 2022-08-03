from flask import render_template
import ssl, smtplib


class User_Email:
    def __init__(self):
        self.username = "admin" 
        self.password = "admin" 

    def send_email(self,sender_email, receiver_email, message):
        port = 465  # For SSL
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, port, context=context) as server:
                server.login(sender_email, self.password)
                server.sendmail(sender_email, receiver_email, message)
            return render_template('success.html')
        except:
            return render_template('failure.html')


class Gmail (User_Email):
    def __init__(self):
        super().__init__()
        self.smtp_server = "smtp.gmail.com"


class Walla (User_Email):
    def __init__(self):
        super().__init__()
        self.smtp_server = "smtp.walla.co.il"


class Yahoo (User_Email):
    def __init__(self):
        super().__init__()
        self.smtp_server = "smtp.yahoo.com"


class MailFactory:
    def factory(self, email_type):
        email_types = {
            "gmail.com": Gmail,
            "walla.co.il": Walla,
            "yahoo.com": Yahoo,
        }
        if email_types.get(email_type):
            return email_types[email_type]() #consructs an object of the corresponding class
        return render_template('failure.html')