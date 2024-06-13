from django.shortcuts import render
from django.http import HttpResponse
from main import getContainers, allContainers, containersInfo, removeAllContainers, removeContainer, runContainer

def your_view(request):
    # Call your Docker function
    result = your_docker_function()
    return HttpResponse(result)