from django.http import HttpResponse
from django.shortcuts import render

# ALL THE LOGIC WRITTEN HERE THAT'S FETCHED BY THE URLS.PY

def home(request):
    # return HttpResponse("Hello this is home page")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("About page yayyyyy")

def contact(request):
    return HttpResponse("contact page yayyy")