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

def set_lang(request):
    next = request.POST.get('next', request.GET.get('next'))
    if ((next or not request.is_ajax()) and
            not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure())):
        next = request.META.get('HTTP_REFERER')
        next = next and unquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
            next = '/'
    response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
    if request.method == 'POST':
        lang_code = request.POST.get(LANGUAGE_QUERY_PARAMETER)
        if lang_code and check_for_language(lang_code):
            if next:
                next_trans = translate_url(next, lang_code)
                response = HttpResponseRedirect(next_trans+"position/1")
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = lang_code
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
            )
    return response