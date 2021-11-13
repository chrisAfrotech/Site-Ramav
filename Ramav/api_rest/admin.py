from django.contrib import admin
from api_rest import models

# Register your models here.

admin.site.register(models.Description)

admin.site.register(models.Membre)
admin.site.register(models.Service)
admin.site.register(models.Projet)
admin.site.register(models.Contact)
admin.site.register(models.Slide)
