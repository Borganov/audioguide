from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home_page.html')

def location(request):
    return render(request, 'location/location.html')
