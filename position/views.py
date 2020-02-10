from django.shortcuts import render

from position.models import Position, PositionItem


def detail(request):
    return render(request, 'position/detail.html')

def positions(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    positions = Position.objects.filter(state=True, lang=lang.id).order_by('order')
    context = {
        'positions': positions,
    }

    return render(request, 'position/positions.html', context)

def positionItem(request):
    positions = PositionItem.objects.filter(state=True, lang=request.LANGUAGE_CODE).order_by('order')
    context = {
        'positionItem': positions,
    }

    return render(request, 'position/positionItem.html', context)
