import schedule
# import time
from django.core.mail import send_mail
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

def appoinment():
    print(' Hello Sir/Madam, your appoinment is fixed...Thank You!! ')

    subject = 'Health Advice From CJC'
    message = 'Hello sir, please wash your hands regularly and be at home stay safe and stay healthy'
    mail_sent = send_mail(subject, message, 'cjc100200300@gmail.com', ['more.shubham203.com', 'abc@gmail.com',
                                        'gopalsadhankar24@gmail.com','borkarmilind22@gmail.com','gurujistudy31@gmail.com'])

    return mail_sent

schedule.every(3).seconds.do(appoinment)


while True:
    schedule.run_pending()
