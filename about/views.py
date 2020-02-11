from django.shortcuts import render

from activity.models import Language


def about(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    return render(request, 'about/about.html')
