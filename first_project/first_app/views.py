from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return  HttpResponse ("Ths is my first django app")

def about(request):
    return HttpResponse("Hello, this is my about page")