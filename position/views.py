from django.shortcuts import render

from activity.models import Language
from position.models import Position, PositionItem
from django.views.generic import  TemplateView


def detail(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    return render(request, 'position/detail.html')

def positions(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    positions = PositionItem.objects.filter(position__isActive=True, lang=lang.id).order_by('position__order')
    print(positions)
    context = {
        'positionItems': positions,
    }

    return render(request, 'position/positions.html', context)

def positionItem(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)

    #Traitement du formulaire
    context = super().get_context_data(**kwargs)

    #Get indicator data
    id = kwargs.get('id')
    positions = PositionItem.objects.get(id=id).__dict__


    return render(request, 'position/positionItem.html', context)


class Detail(TemplateView):
    #set html file to use
    template_name = 'position/positionItem.html'

    def get_context_data(self, **kwargs):
        lang = Language.objects.get(abreviation=self.request.LANGUAGE_CODE)

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        id = kwargs.get('id')
        positionItem = PositionItem.objects.get(id=id).__dict__
        print(positionItem)

        return {'positionItem' : positionItem}
