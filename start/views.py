from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.http import is_safe_url

from activity.models import Activity, Language
import itertools
import json
import os
import re
from urllib.parse import unquote

from django.apps import apps
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context, Engine
from django.urls import translate_url
from django.utils.formats import get_format
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, get_language,
)
from django.utils.translation.trans_real import DjangoTranslation
from django.views.generic import View

LANGUAGE_QUERY_PARAMETER = 'language'


def accueil(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'pages/home_page.html', context)

def start(request):
    lang = Language.objects.get(abreviation=request.LANGUAGE_CODE)
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'pages/start.html', context)