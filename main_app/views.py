from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def about(request):
    return HttpResponse('<h1>I am Taylor the Developer</h1>')