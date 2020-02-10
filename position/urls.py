from django.urls import path

from . import views

urlpatterns = [
    path('', views.positions, name='positions'),
    path('<id>', views.positionItem, name='positionItem'),
    ]