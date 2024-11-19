from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    peoples = [
        {'names': 'yash', 'age': 21},
        {'names': 'pavan', 'age': 22},
        {'names': 'ram', 'age': 15},
        {'names': 'bheem', 'age': 26},
    ]
        
    return render(request, "home/index.html", context={'page': 'Django', 'peoples': peoples})


def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)


def contact(request):
    context = {'page' : 'contact'}
    return render(request, "home/contact.html", context)

def yash_page(request):
    context = {'page' : 'contact'}
    return HttpResponse("<h1>This is yash website</h1>")
