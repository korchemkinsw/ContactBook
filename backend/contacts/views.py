from .models import Communication, Person, Contact
from .serializers import CommunicationSerializer, PersonSerializer, ContactSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
  queryset=Person.objects.all()
  serializer_class=PersonSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
  queryset=Communication.objects.all()
  serializer_class=CommunicationSerializer

class ContactViewSet(viewsets.ModelViewSet):
  queryset=Contact.objects.all()
  serializer_class=ContactSerializer