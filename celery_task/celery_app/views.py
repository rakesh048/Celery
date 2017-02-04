from django.shortcuts import render

# Create your views here.

def celery_function():
	print 'celery task executed'