from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Created my own view!")

# Create your views here.

