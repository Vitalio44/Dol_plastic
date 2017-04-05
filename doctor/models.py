### -*- coding: utf-8 -*- ###
from __future__ import unicode_literals
from django.db import models
from redactor.fields import RedactorField
from django.urls import reverse

class Doctor(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Создано')
    experience= models.CharField(max_length=200, verbose_name='Стаж')
    specialization = models.CharField(max_length=200, verbose_name='Специализация')
    category = models.CharField(max_length=200, verbose_name='Категория')
    content = RedactorField(verbose_name='Контент')
    keywords = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = 'Врача'
        verbose_name_plural = 'Врачи'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.slug

    def get_absolute_url(self):
        return reverse('show_doctor', kwargs={'slug': self.slug})
