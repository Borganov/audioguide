from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from activity.models import Activity, Language
from contact.forms import ContactForm
from position.models import Position
from position.models import PositionItem



def accueil(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'pages/home_page.html', context)

def start(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    languages = Language.objects.all()
    context = {
        'languages': languages,
        'redirect_to' : "accueil"
    }
    return render(request, 'pages/start.html', context)