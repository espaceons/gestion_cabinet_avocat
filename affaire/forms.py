# affaires/forms.py
from django import forms
from .models import Affaire
from clients.models import Client
from utilisateurs.models import Utilisateur

class AffaireForm(forms.ModelForm):
    class Meta:
        model = Affaire
        fields = ['reference', 'client', 'titre', 'description', 'date_ouverture', 'date_cloture', 'statut', 'avocat_responsable']
        widgets = {
            'date_ouverture': forms.DateInput(attrs={'type': 'date'}),
            'date_cloture': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all().order_by('nom')
        self.fields['avocat_responsable'].queryset = Utilisateur.objects.filter(role='AVOCAT').order_by('first_name')