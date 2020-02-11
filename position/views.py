from django.shortcuts import render

from activity.models import Language
from position.models import Position, PositionItem
from django.views.generic import  TemplateView



def positions(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    positions = PositionItem.objects.filter(position__isActive=True, lang=lang.id).order_by('position__order')
    print(positions)
    context = {
        'positionItems': positions,
    }

    return render(request, 'position/positions.html', context)


class Detail(TemplateView):
    #set html file to use
    template_name = 'position/positionItem.html'

    def get_context_data(self, **kwargs):
        lang = Language.objects.get(abreviation=self.request.LANGUAGE_CODE)

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        id = kwargs.get('id')
        positionItem = PositionItem.objects.get(id=id)
        position = Position.objects.get(id = positionItem.position_id).__dict__
        positionItem = positionItem.__dict__
        print(position)


        return {'positionItem' : positionItem, 'position' : position}
