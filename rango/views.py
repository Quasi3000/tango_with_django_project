from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # Import the HttpResponse object from the django.http module
# One view - called index
def index(request): # HttpRequest object named request
    return HttpResponse("Rango says hey there partner!") # Each view must return a HttpResponse object