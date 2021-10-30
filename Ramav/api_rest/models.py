from django.db import models

# Create your models here.

class Description(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField()
    

class Membre(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    metier = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    

class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    video = models.FileField()
    

class Projet(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    video = models.FileField()


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sujet= models.TextField()
    requete = models.TextField()
    tel = models.CharField(max_length=10)
    email = models.EmailField()
    

class Slide(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()

