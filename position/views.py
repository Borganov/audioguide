from django.shortcuts import render

from activity.models import Language
from position.models import Position, PositionItem
from django.views.generic import  TemplateView



def positions(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    positionItems = PositionItem.objects.filter(position__isActive=True, lang=lang.id).order_by('position__order')
    context = {
        'positionItems': positionItems,
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
        idPosition = kwargs.get('id')
        positionItem = PositionItem.objects.filter(position__id=idPosition, lang=lang.id)
        position = Position.objects.get(id = idPosition)
        positions = Position.objects.all()

        current_index = 0
        previousId = 0
        nextId = 0
        #Set Index
        for i,  p in enumerate(positions):
            if str(p.id) == str(idPosition) :
                current_index = i

        #Set hasPrevious
        if current_index > 0:
            hasPrevious = True
            previousId = positions[current_index - 1].id
        else :
            hasPrevious = False
            previousId = -1

        #Set hasNext
        if current_index < len(positions)-1:
            hasNext = True
            nextId = positions[current_index + 1].id
        else :
            hasNext = False


        context = {
            'positionItem': positionItem[0],
            'position' : position.__dict__,
            'nextId' : nextId,
            'previousId' : previousId,
            'hasNext' : hasNext,
            'hasPrevious' : hasPrevious,
            }

        print(context)


        return context
