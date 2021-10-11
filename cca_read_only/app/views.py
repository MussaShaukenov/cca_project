from django.shortcuts import render
from django.http import HttpResponse
from . models import WebsiteUser


# nginx port: 8080
def index(request):
    return HttpResponse('Read app Welcome Page')

# ports 7001, 7002, 7003
def get_names(request):
    all_objects = WebsiteUser.objects.all()
    context = {'context': all_objects}
    return HttpResponse(all_objects.order_by('id'))
