from django import forms
from django.forms.models import inlineformset_factory

from .models import Contact, PersonContact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ('type', 'contact',)
    exclude = ()

class PersonContactsForm:
  class Meta:
    model = PersonContact
    fields = ('contact')
    exclude = ('person')

ContactFormset = inlineformset_factory(PersonContact, Contact, form = ContactForm, extra=1)
