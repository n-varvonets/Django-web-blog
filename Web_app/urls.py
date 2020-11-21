#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        re_path('^admin/', admin.site.urls),
        path(r'news/', include('news.urls')),
        path(r'', include('main.urls'))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # add an ability to connect static files
