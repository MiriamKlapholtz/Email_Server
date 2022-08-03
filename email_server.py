from flask import Flask, request, render_template
import re
from classes import MailFactory


def is_valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
    return re.fullmatch(regex, email)

app = Flask(__name__)

@app.route('/')
def home():
    return "Wellcom to the email server"

@app.route('/send_email',methods = ['POST'])
def send_email():
    receiver_email = request.form['receiver_email']
    sender_email = request.form['sender_email']
    message = request.form['message']

    if(is_valid_email(sender_email)):
        email_type = sender_email.split("@")[1]
        mail_obj = MailFactory().factory(email_type) #constructs an object of the corresponding class
        return mail_obj.send_email(sender_email, receiver_email, message)

    return render_template('failure.html')

if __name__ == "__main__":
    app.run()