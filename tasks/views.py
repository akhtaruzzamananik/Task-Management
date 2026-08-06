from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System!")

def contacts(request):
    return HttpResponse("<h1 style='color: blue;'>Contact Information</h1><p>Here is the contact information.</p>")

def show_task(request):
    return HttpResponse("<h1 style='color: green;'>Task Details</h1><p>Here are the details of the task.</p>")  
