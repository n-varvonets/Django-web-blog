# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render


def index(request):  # we can pass data in html using Jinja
    data = {
        'title': 'Home page',
        'values': ['1.)Like LIST', 'Array', 'some', 'data', 'which', 'we,', 'put', 'in', 'index', 'html', 'using',
                   'цикл'],
        'dict_obj': {
            '2.1)Like DICT(key)+ ньюнас - ': '2.2)пример словаря(value) + слварь выводит без порядочно',
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def settings(request):
    return render(request, 'main/settings.html')


def contacts(request):
    return render(request, 'main/contacts.html')
