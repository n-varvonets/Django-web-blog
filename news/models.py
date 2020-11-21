# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''миграция - синхронизация  нашего проекта с БД. Для этого необходимо создать python manage.py makemigrations,
и теперь когда создан сам файл миграции, можно провести сами миграции. Потом перейти  admin.py и зарегай созданный ниже класс'''

''' что бы создать таблицу в БД нужно создать класс, кеоторый будет из себя представлять модель,
 а модель в свою очередь - это определенная таблица в БД, поэтому данно такое название скрипту'''


class Articles(
    models.Model):  # в 1)аргементе наследуемся от класса Model и если не указать,то мы не создадим коректный класс, а
    # только саму по себе  модель    #  2)далее указываем поля новости, где я хочу хранить 4 апараметра: а) название, б) анонс, в)полный текст, г)дату публикации
    title = models.CharField('Name',
                             max_length=50)  # CharField() - поле(класс) в БД, что хранит не более  255 символов, в аргументе указываем доп инфу(венутри поля будет светиться название и макс длина 50 символов)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Full text')
    date = models.DateTimeField('Date of publication')

    '''необходимо добавить метод, который будет переадресовывать пользователя на страничку, после добавления
    или редактирования статьи'''

    def get_absolute_url(self):
        return f'/news/{self.id}'  # необходимо доавить f- format, для отобрабрежения url.id при переадресации на собновленную статью(если не указать, то нас переадресует на news_home.html)

    def __str__(
            self):  # указываем какая информация будет выводится при вызове(get) обьекта с БД, (если не укзать, то будут выводиться object1, object2, ....))
        return self.title

    '''и т.к. в admin/ джанго добавляет к названию по умлочнаиию букву s, то есть смысл заранее назвать нашу таблицу'''

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
