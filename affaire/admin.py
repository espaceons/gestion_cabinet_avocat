# affaires/admin.py
from django.contrib import admin
from .models import Affaire

@admin.register(Affaire)
class AffaireAdmin(admin.ModelAdmin):
    list_display = ('reference', 'titre', 'client', 'statut', 'date_ouverture', 'avocat_responsable')
    list_filter = ('statut', 'date_ouverture', 'avocat_responsable')
    search_fields = ('reference', 'titre', 'client__nom', 'description')
    raw_id_fields = ('client', 'avocat_responsable') # Pour les FK avec beaucoup d'éléments
    date_hierarchy = 'date_ouverture'