from django.urls import path


from . import views

urlpatterns = [
    path('', views.positions, name='positions'),
    path('<id>', views.Detail.as_view(), name='activity'),
    ]
