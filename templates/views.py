from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from contact.forms import ContactForm


def home(request):
    from django.utils import translation

    return render(request, 'pages/home_page.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            subject_name = form.cleaned_data['subject']
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} vous a envoyé un message - son email est {1} \n\nSon message : \n\n{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail(subject_name, message, sender_email, ['nadine.waelti1990@gmail.com'], fail_silently=False)
            return HttpResponse('Merci d''avoir pris contact avec nous!')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


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