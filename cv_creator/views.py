from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    return HttpResponse("Create CV form")