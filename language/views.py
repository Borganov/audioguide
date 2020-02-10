from django.shortcuts import render

from activity.models import Language


def language(request):
    languages = Language.objects.All()
    context = {
        'abreviation': languages,
    }
    return render(request, 'language/language.html', context)
