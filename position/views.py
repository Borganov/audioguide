from django.shortcuts import render

from activity.models import Language
from position.models import Position, PositionItem


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
    positions = PositionItem.objects.filter(state=True, lang=lang.id).order_by('order')
    context = {
        'positionItem': positions,
    }

    return render(request, 'position/positionItem.html', context)
