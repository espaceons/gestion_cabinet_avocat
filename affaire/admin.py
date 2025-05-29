from django.contrib import admin
from .models import Affaire

class AffaireAdmin(admin.ModelAdmin):
    list_display = ('reference', 'titre', 'client', 'avocat_responsable', 'statut')
    list_filter = ('statut', 'avocat_responsable')
    search_fields = ('reference', 'client__nom', 'titre')
    raw_id_fields = ('client',)  # Pour les relations avec beaucoup d'instances

admin.site.register(Affaire, AffaireAdmin)