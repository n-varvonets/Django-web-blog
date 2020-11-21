#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# прописываем ту часть которая идет после news/...
urlpatterns = [

    path(r'<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),    # pk - primary_key и важно записать без пробелов + указываем что вызываем не метод, а уже КЛАСС дполнительно указав .as_view()
    path(r'<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path(r'<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path(r'create', views.create, name='create'),
    path(r'', views.news_home, name='news_home'),

]