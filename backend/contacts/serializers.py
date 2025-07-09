from django.db import transaction
from rest_framework import serializers
from .models import Communication, Person, Contact

class CommunicationSerializer(serializers.ModelSerializer):
  class Meta:
    model=Communication
    fields=('channel', 'tool')

class ContactSerializer(serializers.ModelSerializer):
  communication=CommunicationSerializer()
  class Meta:
    model = Contact
    fields=('communication', 'type', 'note')

class PersonSerializer(serializers.ModelSerializer):
  contacts=ContactSerializer(many=True)
  class Meta:
    model=Person
    fields=('id', 'avatar', 'name', 'contacts')

  def create_contacts(self, person, contacts_data):
    Contact.objects.bulk_create([
      Contact(
        person=person,
        communication=Communication.objects.get_or_create(**contact_data['communication'])[0],
        type=contact_data['type'],
        note=contact_data['note']
      ) for contact_data in contacts_data
    ])

  @transaction.atomic
  def create(self, validated_data):
    contacts=validated_data.pop('contacts')
    person=Person.objects.create(**validated_data)
    person.save()
    self.create_contacts(person, contacts)
    return person

  @transaction.atomic
  def update(self, instance, validated_data):
    contacts=validated_data.pop('contacts')
    Contact.objects.filter(person=instance).delete()
    self.create_contacts(instance, contacts)
    super().update(instance, validated_data)
    return instance
  