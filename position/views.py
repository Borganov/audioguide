from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  TemplateView
from audioguide import settings

from .models import PositionItem
