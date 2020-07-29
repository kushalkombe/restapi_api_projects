#from django_email_celery.celery import app
from time import sleep
from django.core.mail import send_mail



#@app.task
def send_email_task():

    # x=send_mail('well done',
    #             'very good',
    #             'abc@gmail.com',
    #             ['xyz@gmail.com'])
    print('hello')

    #return x
