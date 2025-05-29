# calendrier/admin.py
from django.contrib import admin
from .models import RendezVous

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin', 'affaire', 'display_participants')
    list_filter = ('date_debut', 'affaire')
    search_fields = ('titre', 'description', 'affaire__reference')
    filter_horizontal = ('participants',) # Pour une meilleure gestion des ManyToMany

    def display_participants(self, obj):
        return ", ".join([participant.get_full_name() for participant in obj.participants.all()])
    display_participants.short_description = 'Participants'