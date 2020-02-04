from django.http import HttpResponse
from django.shortcuts import render


def activity(request):
    return render(request, 'activity/activity.html')