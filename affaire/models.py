from django.db import models

from clients.models import Client

# Create your models here.
class Affaire(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    date_ouverture = models.DateField()
    statut = models.CharField(choices=[("EN_COURS", "En cours"), ("CLOTURE", "Clôturé"), ("ANNULE", "Annulé")])
    description = models.TextField()