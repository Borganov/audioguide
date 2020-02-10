from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from activity.models import Activity, Language
from contact.forms import ContactForm
from position.models import Position
from position.models import PositionItem



def accueil(request):
    return render(request, 'pages/home_page.html')

def start(request):
    return render(request, 'pages/start.html')