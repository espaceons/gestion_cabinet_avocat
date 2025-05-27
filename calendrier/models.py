from django.db import models

from affaire.models import Affaire
from utilisateurs.models import Utilisateur

# Create your models here.
class RendezVous(models.Model):
    affaire = models.ForeignKey(Affaire, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    participants = models.ManyToManyField(Utilisateur)