from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('accueil/', views.accueil, name='home_page'),
]
