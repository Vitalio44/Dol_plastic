### -*- coding: utf-8 -*- ###
from __future__ import unicode_literals
from django.db import models
from redactor.fields import RedactorField


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создано')
    menu_name = models.CharField(max_length=80, verbose_name='Название в меню')
    menu_position = models.IntegerField(verbose_name='Позиция в меню', null=True, blank=True, unique=True)
    content = RedactorField(verbose_name='Контент')
    keywords = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = 'Сраницу'
        verbose_name_plural = 'Страницы'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.slug


class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создано')
    content = RedactorField(verbose_name='Контент')
    slide_position = models.IntegerField(verbose_name='Позиция', null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображене')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title


class MainMenu(models.Model):
    menu_name = models.CharField(max_length=128, verbose_name='Имя в меню')
    url = models.URLField(verbose_name='Ссылка настраницу')
    menu_position = models.IntegerField(verbose_name='Позиция в меню', unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.menu_name