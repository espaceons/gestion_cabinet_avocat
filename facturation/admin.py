# facturation/admin.py
from django.contrib import admin
from .models import Facture

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'affaire', 'montant', 'date_emission', 'statut_paiement')
    list_filter = ('statut_paiement', 'date_emission')
    search_fields = ('affaire__reference',)
    raw_id_fields = ('affaire',)
    date_hierarchy = 'date_emission'