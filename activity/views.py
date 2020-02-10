from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Language, ActivityItem


def activity(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    activities = ActivityItem.objects.filter(isActive=True, lang=lang.id).order_by('activity__number')
    context = {
        'activities': activities,
    }
    return render(request, 'activity/activities.html', context)

def activityItem(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)

    #Traitement du formulaire
    context = super().get_context_data(**kwargs)

    #Get indicator data
    id = kwargs.get('id')
    activities = ActivityItem.objects.get(id=id).__dict__


    return render(request, 'activity/activityItem.html', context)


class Detail(TemplateView):
    #set html file to use
    template_name = 'activity/activityItem.html'

    def get_context_data(self, **kwargs):
        lang = Language.objects.get(abreviation=self.request.LANGUAGE_CODE)

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)

        #Get indicator data
        id = kwargs.get('id')
        activityItem = ActivityItem.objects.get(id=id).__dict__
        print(activityItem)

        return {'activityItem' : activityItem}

