"""audioguide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('about/', include('about.urls')),
    path('activity/', include('activity.urls')),
    path('contact/', include('contact.urls')),
    path('position/', include('position.urls')),
    path('set_lang/', include('start.urls')),
    path('', include('start.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
