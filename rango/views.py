from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # Import the HttpResponse object from the django.http module
# One view - called index
def index(request): # HttpRequest object named request
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>") # Each view must return a HttpResponse object
    # hyperlink?

# view method called about
def about(request): # about page
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>") # <br/>? <a>? </a>?
    # link back?