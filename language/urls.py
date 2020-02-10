from django.urls import path

from . import views

urlpatterns = [
    path('language', views.language, name='langues'),
]
