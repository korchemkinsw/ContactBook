from django.contrib import admin
from .models import (Communication, Person, Contact)

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
  list_display = (
    'channel',
    'tool',
  )
  search_fields = ['tool']
  list_filter = ['tool']
  empty_value_display = '-пусто-'

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
  list_display = (
    'person',
    'communication',
    'type',
    'note',
  )
  empty_value_dysplay = '-пусто-'

class ContactInline(admin.TabularInline):
  model = Contact
  min_num = 1
  extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  list_display = (
    'avatar',
    'name',
  )
  search_fields = ['name']
  list_filter = ['name']
  inlines = [ContactInline]
  empty_value_display = '-пусто-'
