from django.db import models
from django.core.validators import MinValueValidator
from clients.models import Client
from utilisateurs.models import Utilisateur  # Import de votre modèle personnalisé

class Affaire(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('PAYE', 'Payé'),
        ('PARTIELLEMENT_PAYE', 'Partiellement payé'),
        ('ANNULE', 'Annulé'),
        ('CLOTURE', 'Clôturé'),
    ]

    client = models.ForeignKey( Client, on_delete=models.CASCADE, verbose_name="Client associé", related_name="affaires")
    
    reference = models.CharField( max_length=50, unique=True, verbose_name="Référence de l'affaire")
    
    date_ouverture = models.DateField( verbose_name="Date d'ouverture", null=True, blank=True)
    
    statut = models.CharField( max_length=20, choices=STATUT_CHOICES, verbose_name="Statut de l'affaire", default='EN_ATTENTE')
    
    description = models.TextField( verbose_name="Description détaillée", blank=True )
    
    avocat_responsable = models.ForeignKey(
        Utilisateur,  # Utilisation de votre modèle personnalisé
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Avocat responsable",
        related_name="affaires_en_charge",
        limit_choices_to={'role': 'AVOCAT'}  # Restreint le choix aux utilisateurs avec rôle AVOCAT
    )
    
    titre = models.CharField( max_length=200, verbose_name="Titre de l'affaire" )
    
    date_cloture = models.DateField( verbose_name="Date de clôture", null=True, blank=True )
    
    frais = models.DecimalField( max_digits=10, decimal_places=2, verbose_name="Frais juridiques", default=0.00, validators=[MinValueValidator(0)] )

    class Meta:
        verbose_name = "Affaire"
        verbose_name_plural = "Affaires"
        ordering = ['-date_ouverture']
        permissions = [
            ("changer_statut", "Peut modifier le statut des affaires"),
            ("voir_toutes_affaires", "Peut voir toutes les affaires (même celles des autres avocats)"),
        ]

    def __str__(self):
        return f"{self.reference} - {self.titre} ({self.client.nom})"

    def est_cloturee(self):
        return self.statut == 'CLOTURE' and self.date_cloture is not None

    def save(self, *args, **kwargs):
        """Override de la méthode save pour logique métier"""
        # Exemple : Auto-clôture si statut est CLOTURE mais date non renseignée
        if self.statut == 'CLOTURE' and not self.date_cloture:
            from django.utils import timezone
            self.date_cloture = timezone.now().date()
        super().save(*args, **kwargs)