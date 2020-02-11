from django.urls import path


from . import views

urlpatterns = [
    path('', views.activity, name='activities'),
    path('<id>', views.Detail.as_view(), name='activity'),
    ]
