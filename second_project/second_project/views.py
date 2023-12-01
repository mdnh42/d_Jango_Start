from django.http import HttpResponse


def home(request):
    return httpResponse("this is my home page")