from django.shortcuts import render
from django.http import HttpResponse
from . models import WebsiteUser


# nginx port: 8080
def index(request):
    return HttpResponse('Write app Welcome Page')

# ports: 8001, 8002, 8003
def add_name(request):
    new_user = WebsiteUser()
    name = request.GET.get('name')
    new_user.name = name
    new_user.save()
    return HttpResponse(name)


