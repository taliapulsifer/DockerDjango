from django.shortcuts import render, HttpResponse

# Create your views here.

# A function that returns some kind of response. Could render html or return httpresponses
def home(request):
    #return HttpResponse("hello world!")
    return render(request, "home.html")
    #Need to connect through a root or url in the urls.py