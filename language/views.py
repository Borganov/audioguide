from django.shortcuts import render

from activity.models import Language


def language(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'language/language.html', context)
