from django.shortcuts import render

from .models import Activity, Language


def activity(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    activities = Activity.objects.filter(isActive=True, lang=lang.id).order_by('number')
    context = {
        'activities': activities,
    }
    return render(request, 'activity/activities.html', context)
