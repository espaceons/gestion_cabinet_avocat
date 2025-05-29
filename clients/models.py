# models.py
from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    type_client = models.CharField(choices=[("PARTICULIER", "Particulier"), ("ENTREPRISE", "Entreprise")], max_length=20) # Ajout de max_length
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom