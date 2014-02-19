from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hello(request):
    """
    hello: request object -> HttpResponse object
    This is our view function. Takes at least on parameter, called request. 
    This is an object that contains info about current Web request, and it's 
    an instance of the class django.http.HttpRequest.    
    """
    
    return HttpResponse("Hello world")

def homepage(request):
    return HttpResponse("Homepage!")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,hour):
    try:
        hours = int(hour) # b/c the regex will be a string
    except ValueError:
        raise Http404()
    return HttpResponse("You entered %i" % hours)
    

