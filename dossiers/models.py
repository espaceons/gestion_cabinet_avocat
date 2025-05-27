from django.db import models

from affaire.models import Affaire

# Create your models here.
class Document(models.Model):
    affaire = models.ForeignKey(Affaire, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to="documents/")
    date_upload = models.DateTimeField(auto_now_add=True)