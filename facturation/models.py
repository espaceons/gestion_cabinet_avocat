from django.db import models

from affaire.models import Affaire

# Create your models here.
class Facture(models.Model):
    affaire = models.ForeignKey(Affaire, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_emission = models.DateField()
    statut_paiement = models.CharField(choices=[("PAYE", "Payé"), ("EN_ATTENTE", "En attente"), ("PAYEMENT_PARTIEL", "Payement partiel")])