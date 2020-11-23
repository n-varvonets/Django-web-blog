from django.urls import path
from . import views

urlpatterns = [

    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('my_contact', views.my_contact, name='my_contact'),
    path('', views.index, name='home')

]
