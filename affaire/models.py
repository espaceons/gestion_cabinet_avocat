from django.db import models
from clients.models import Client

class Affaire(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('PAYE', 'Payé'),
        ('PARTIELLEMENT_PAYE', 'Partiellement payé'),
        ('ANNULE', 'Annulé'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client associé")
    reference = models.CharField(max_length=50, unique=True, verbose_name="Référence de l'affaire") # Ajout de unique=True
    date_ouverture = models.DateField(verbose_name="Date d'ouverture")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, verbose_name="Statut de l'affaire")
    description = models.TextField(verbose_name="Description détaillée")

    def __str__(self):
        return f"{self.reference} - {self.client.nom}"