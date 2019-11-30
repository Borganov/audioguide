from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>', views.Detail.as_view(), name='activity'),
]
