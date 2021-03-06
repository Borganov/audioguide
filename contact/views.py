from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

from activity.models import Language
from contact.forms import ContactForm


def contact(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['berclazalexandre@gmail.com'],
                fail_silently=False,
            )



            # send email code goes here
            #subject_name = form.cleaned_data['subject']
            #sender_name = form.cleaned_data['name']
            #sender_email = form.cleaned_data['email']
            #message = "{0} vous a envoyé un message - son email est {1} \n\nSon message : \n\n{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            #send_mail(subject_name, message, sender_email, ['nadine.waelti1990@gmail.com'], fail_silently=False)
            return HttpResponse('Merci d''avoir pris contact avec nous!')


    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
