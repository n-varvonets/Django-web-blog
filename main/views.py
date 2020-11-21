# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# то юбы передать данные в хтмл нужно в рендер передать третий параметр(ключ:значение) и в templates исп. jinja
def index(request):
    data = {
        'title': 'Главная старница',
        'values': ['1.)пример списка','Array','some','data','which','we,','put','in','index','html','using', 'цикл'],
        'dict_obj': {
                      '2.1)пример словаря(key)+ ньюнас - ':'2.2)пример словаря(value) + слварь выводит без порядочно',
                      'car': 'BMW',
                      'age':18,
                      'hobby':'football'
                      }

    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def settings(request):
    return render(request,'main/settings.html')

def contacts(request):
    return render (request, 'main/contacts.html')
