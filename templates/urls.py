from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('accueil', views.accueil, name='home_page'),
    path('location', views.location, name='location'),
    path('position', views.positions, name='positions'),
    path('activity', views.activity, name='activity'),
    path('about', views.about, name='about'),
    path('language', views.language, name='langues'),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('don', views.don, name='don'),
]
