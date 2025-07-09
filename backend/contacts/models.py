import os
from django.db import models
  
class Communication(models.Model):
  COMMUNICATIONS = {
    "PM": "телефон мобильный",
    "PS": "телефон стационарный",
    "EM": "электронная почта",
  }

  channel = models.CharField(
    max_length=2,
    choices=COMMUNICATIONS,
    verbose_name='канал связи',
  )
  tool = models.CharField(
    max_length=20,
    verbose_name='контакт',
    unique=False,
  )

  class Meta:
    verbose_name='Коммуникация'
    verbose_name_plural='Коммуникация'

  def __str__(self):
    return f'{self.channel}: {self.tool}'
  
class Person(models.Model):
  name = models.CharField(
    max_length=100,
    verbose_name='Имя',
  )
  avatar = models.ImageField(
    blank=True,
    null=True,
    upload_to='contact_media',
    verbose_name='Аватар'
  )

  class Meta:
    verbose_name = 'Лицо'
    verbose_name_plural = 'Лица'
    ordering = ['name']

  def __str__(self):
    return self.name

class Contact(models.Model):
  TYPE = {
    "PR": "личный",
    "PU": "служебный" 
  }
  person = models.ForeignKey(
    Person,
    on_delete=models.CASCADE,
    verbose_name='Имя',
    related_name='contacts'
  )  
  communication = models.ForeignKey(
    Communication,
    on_delete=models.CASCADE,
    verbose_name='Контакт',
    #related_name='contacts',
  )
  type = models.CharField(
    max_length=2,
    choices=TYPE,
    verbose_name='Тип контакта',
  )
  note = models.CharField(
    max_length=100,
    blank=True,
    verbose_name='Комментарий'
  )

  class Meta:
    verbose_name='Контакт'
    verbose_name_plural='Контакты'

    def __str__(self):
      return f'{self.person.name} - {self.contact.channel}: {self.contact.tool}'
  