from celery_example.celery import app
#from .task import test_celery

@app.task
def add(x,y):
	return x + y

@app.task
def sleeptask(i):
	from time import sleep
	sleep(i)
	return i
