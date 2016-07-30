"""InstaClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import absolute_import
from django.conf.urls import url,include
from django.contrib import admin

from InstaApp import views
from signup.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view


urlpatterns = [
    url(r'^adm/', admin.site.urls),
    url('', include('django.contrib.auth.urls')),
    url(r'^$',auth_view.login),
    url(r'', include('InstaApp.urls', namespace='posts')),
    url(r'^Logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    # url(r'^home/$', home,name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
