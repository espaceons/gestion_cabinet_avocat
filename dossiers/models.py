from django.db import models
from affaire.models import Affaire
from django.utils import timezone

from utilisateurs.models import Utilisateur

class Document(models.Model):
    affaire = models.ForeignKey( Affaire,  on_delete=models.CASCADE, related_name='documents', verbose_name="Affaire associée" )
    titre = models.CharField(max_length=200, verbose_name="Titre du document")
    fichier = models.FileField( upload_to="documents/%Y/%m/%d/", verbose_name="Fichier" )
    date_upload = models.DateTimeField( auto_now_add=True, verbose_name="Date d'upload" )
    description = models.TextField( blank=True, verbose_name="Description" )
    uploader = models.ForeignKey( Utilisateur, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Uploader" )

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-date_upload']

    def __str__(self):
        return f"{self.titre} - {self.affaire.reference}"

    def extension(self):
        import os
        name, extension = os.path.splitext(self.fichier.name)
        return extension.lower()