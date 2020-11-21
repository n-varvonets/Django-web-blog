from django.urls import path
from . import views

urlpatterns = [

    path('about', views.about, name='about'),
    path('settings', views.settings, name='settings'),
    path('contacts', views.contacts, name='contacts'),
    path('', views.index, name='home')

]
