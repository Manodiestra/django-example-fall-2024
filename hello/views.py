from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
    

def user_form(request):
    return render(request, 'hello/dynamic_stuff.html')

