from django.db import models

from affaire.models import Affaire

# Create your models here.
class Facture(models.Model):
    affaire = models.ForeignKey(
        Affaire,
        on_delete=models.CASCADE, # Ou models.SET_NULL, selon votre logique métier
        related_name='factures',  # <-- Le related_name que vous voulez
        verbose_name="Affaire associée"
    )
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_emission = models.DateField()
    statut_paiement = models.CharField(choices=[("PAYE", "Payé"), ("EN_ATTENTE", "En attente"), ("PAYEMENT_PARTIEL", "Payement partiel")], max_length=20) # Ajout de max_length

    def __str__(self):
        return f"Facture #{self.id} - {self.affaire.reference} - {self.montant} {self.statut_paiement}"