from pyexpat import model

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Language, ActivityItem, Activity


def activity(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    activityItems = ActivityItem.objects.filter(isActive=True, lang=lang.id).order_by('activity__prestataire','activity__number', 'order')
    print(activityItems)

    context = {
        'activityItems': activityItems,
    }
    return render(request, 'activity/activities.html', context)


class Detail(TemplateView):
    #set html file to use
    template_name = 'activity/activityItem.html'

    def get_context_data(self, **kwargs):
        lang = Language.objects.get(abreviation=self.request.LANGUAGE_CODE)

        #Traitement du formulaire
        context = super().get_context_data(**kwargs)


        #Get indicator data
        id = kwargs.get('id')
        activityItem = ActivityItem.objects.get(id=id)
        activity = Activity.objects.get(id=activityItem.activity_id).__dict__
        print(activity)
        activityItem = activityItem.__dict__

        return {'activityItem' : activityItem, 'activity':activity}

