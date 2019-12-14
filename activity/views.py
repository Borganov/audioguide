from django.http import HttpResponse
from django.views.generic import  TemplateView
from audioguide import settings

from .models import Activity

def index(request):
    toPrint = Activity.objects.get(title="Titre1")
    idInText = str(toPrint.id)
    print(toPrint)
    return HttpResponse("activity n° 1, Titre: " + toPrint.title + " description : " + idInText)


class Detail(TemplateView):
    #set html file to use
    template_name = 'activity/detail.html'

    def get_context_data(self, **kwargs):

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        id = kwargs.get('id')
        context = Activity.objects.get(id=id).__dict__
        print(context)

        return context

class All(TemplateView):
    #set html file to use
    template_name = 'activity/activities.html'

    def get_context_data(self, **kwargs):

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        lg = kwargs.get('lg')
        context = Activity.objects.filter(lang__startswith=lg)

        print(context)

        print({'activities' : context})

        return {'activities' : context}
