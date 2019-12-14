from django.http import HttpResponse
from django.views.generic import  TemplateView
from audioguide import settings

from .models import PositionItem

# Create your views here.
class Detail(TemplateView):
    #set html file to use
    template_name = 'position/detail.html'

    def get_context_data(self, **kwargs):

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        id = kwargs.get('id')
        context = PositionItem.objects.get(id=id).__dict__
        print(context)

        return context

class All(TemplateView):
    #set html file to use
    template_name = 'position/positions.html'

    def get_context_data(self, **kwargs):

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        lg = kwargs.get('lg')
        context = PositionItem.objects.filter(lang__startswith=lg)


        return {'positions' : context}
