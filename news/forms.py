# -*- coding: utf-8 -*-
# создал этот файл для того что бы свзяать файл create/форму для связи с БД(модели Articles), которую опишем внутри этого файла

# логично нужно импортировать таблицу из БД(модель Articles)
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea



'''Класс можно назвать как угодно, но обычно это название модели и в конце Form'''
class ArticlesForm(ModelForm):  #  +наследуемся от импортируемого класса
    '''внутри класса немобхоимо создать вложенный класс Meta, внутри которого указываем характеристики таблицы'''
    class Meta:
        model = Articles #  указываем с какой моделью/таблицой мы работаем
        fields = ['title', 'anons', 'full_text', 'date'] # указываем какие поля должны быть выведены внутри формы

        # прежде чем это всё тестировать , необходимо создать обьект на основе этого класса и передать его
        # в сам шаблон(для отображения формы связи с нужной для нас таблицы/модели). Во views созхдаем этот обьект.

        '''указываем как отоброжать наши данные в html с помощью атрибутов placeholder, class, etc.., таким же образом как и create.html'''
        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Title of article' # почему с русским тектом не отоброжается поле


            }),
            'anons': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Anons of article'
                }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full text of article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd hh:mm:ss'

            })
        }


