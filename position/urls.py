from django.urls import path

from . import views

urlpatterns = [
    path('position', views.positions, name='positions'),
    path('positionItem', views.positionItem, name='positionItem'),
    ]