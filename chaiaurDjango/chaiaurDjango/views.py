from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World. You are at chai aur Djange Home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello World. You are at chai aur Djange About page")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("Hello World. You are at chai aur Djange Contact page")
    return render(request, 'website/contact.html')