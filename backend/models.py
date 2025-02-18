from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField(max_length=12)

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    pokedex_number = models.IntegerField()
    primary_type = models.CharField(max_length=15)
    secondary_type = models.CharField(max_length=15, null=True, blank=True)
    Imagen_pokemon = models.ImageField(upload_to='pokemon_images/', null=True,blank=True)
