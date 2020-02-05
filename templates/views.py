from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home_page.html')


def accueil(request):
    return render(request, 'pages/home_page.html')


def location(request):
    return render(request, 'location/location.html')


def positions(request):
    return render(request, 'position/positions.html')


def activity(request):
    return render(request, 'activity/activities.html')


def about(request):
    return render(request, 'about/about.html')


def language(request):
    return render(request, 'language/language.html')