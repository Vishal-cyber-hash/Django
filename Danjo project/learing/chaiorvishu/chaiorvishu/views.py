from django.http  import HttpResponse
from django.shortcuts import render 

def home(request):
    # return HttpResponse("Hello, world, Welcome to home page..")
    return render(request, "index.html")

def about(request):
    return HttpResponse("Hello, world, welcome to about page")
def blog(request):
    return HttpResponse("Hello, world, welcome to blog page.")
