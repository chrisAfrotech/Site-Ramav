from django.db.models import fields
from rest_framework import serializers
from api_rest import models


class DescriptionSerialser(serializers.ModelSerializer):
    
    class Meta:
        model = models.Description
        fields = ["id","text", "image"]
    

class MembreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Membre
        fields = ["id", "nom", "prenom", "fonction", "metier", "image"]
    

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Service
        fields = ["id", "nom", "description", "image", "video"]


class ProjetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Projet
        fields = ["id", "nom", "description", "image", "video"]


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Contact
        fields = ["id", "nom", "prenom", "sujet", "requete", "tel", "email"]


class SlideSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Slide
        fields = ["id", "image1", "image2", "image3", "image4", "image5"]


