from django.shortcuts import render
# Create your views here.

def home(request):
    title = "welcome to home page"
    context = {title:'title'}

    return render (request , 'home.html' , context)
