from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('accueil', views.accueil, name='accueil'),
    path('set_lang', views.set_lang, name='set_lang'),
]
