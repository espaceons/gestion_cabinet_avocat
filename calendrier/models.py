from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from affaire.models import Affaire

User = get_user_model()

class RendezVous(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=200, blank=True)
    affaire = models.ForeignKey( Affaire, on_delete=models.SET_NULL, null=True, blank=True, related_name='rendezvous', verbose_name="Affaire associée" )
    participants = models.ManyToManyField(User, related_name='rendez_vous', null=True, blank=True)
    createur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rendez_vous_crees')

    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
        ordering = ['date_debut']

    def __str__(self):
        return f"{self.titre} - {self.date_debut}"