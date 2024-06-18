from django.shortcuts import render, HttpResponse
from .models import TodoItem
from . import dockerFunctions

# Create your views here.

# A function that returns some kind of response. Could render html or return httpresponses
def home(request):
    #return HttpResponse("hello world!")
    return render(request, "home.html")
    #Need to connect through a root or url in the urls.py

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def runContainer(request):
    if request.method == "POST":
        image_name = request.POST.get('image_name')
        if not image_name:
            return HttpResponse("Error: No image name provided", status=400)
        try:
            dockerFunctions.runContainer(imageName=image_name)
            return HttpResponse("Container started successfully")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)
    return render(request, 'mainApp/home.html')