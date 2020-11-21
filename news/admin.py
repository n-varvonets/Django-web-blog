# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Articles # импортируем с модели(свзязи с БД) созданную таблицу Articles

admin.site.register(Articles)


