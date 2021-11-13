from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin) #, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from api_rest import serializers
from api_rest import models


class DescriptionViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = serializers.DescriptionSerialser
    queryset = models.Description.objects.all()


class MembreViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = serializers.MembreSerializer
    queryset = models.Membre.objects.all()


class ServiceViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = serializers.ServiceSerializer
    queryset = models.Service.objects.all()


class ProjectViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = serializers.ProjetSerializer
    queryset = models.Projet.objects.all()


class ContactViewSet(CreateModelMixin, GenericViewSet):
    
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()


class SlideViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = serializers.SlideSerializer
    queryset = models.Slide.objects.all()

