# app/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, welcome to the index page!")
