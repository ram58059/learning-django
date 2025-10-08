from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greet_hello(request):
    return HttpResponse("Hello, welcome to Geeks World!")