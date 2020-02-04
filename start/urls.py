from django.urls import path

from . import views
from activity import views as views_activity
from post import views as views_post

urlpatterns = [
    path('', views.start, name='Accueil'),
    path('language/', views.language, name='language'),
    path('aide/', views.aide, name='aide'),
    path('activity/', views_activity.activity, name='activités'),
    path('post/', views_post.post, name='audioguide'),
]
