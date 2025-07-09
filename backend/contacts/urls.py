from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunicationViewSet, PersonViewSet, ContactViewSet
router=DefaultRouter()
router.register(r'communication', CommunicationViewSet, basename='communication')
router.register(r'contactsbook', PersonViewSet, basename='contactsbook')
router.register(r'contact', ContactViewSet, basename='contakt')


urlpatterns=[
  path('', include(router.urls)),
]
