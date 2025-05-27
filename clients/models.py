# models.py
from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    type_client = models.CharField(choices=[("PARTICULIER", "Particulier"), ("ENTREPRISE", "Entreprise")])
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()