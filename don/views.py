from django.shortcuts import render

from activity.models import Language


def don(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    return render(request, 'don/don.html')
