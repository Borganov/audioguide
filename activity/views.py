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
        id = '='+kwargs.get('id')
        context = Activity.objects.get(id='1').__dict__

        return context
