# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''python manage.py makemigrations - put it in terminal for making migration between DB and script'''


class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.TextField('Anons')
    full_text = models.TextField('Full text')
    date = models.DateTimeField('Date of publication')

    '''a method that redirects the user after adding or editing an article'''

    def get_absolute_url(self):
        return f'/news/{self.id}'  # f- format for rendering id in url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
