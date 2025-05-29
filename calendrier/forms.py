from django import forms
from .models import RendezVous
from utilisateurs.models import Utilisateur
from django.utils import timezone

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['titre', 'description', 'date_debut', 'date_fin', 'lieu', 'participants']
        widgets = {
            'date_debut': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'date_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = Utilisateur.objects.exclude(id=user.id) if user else Utilisateur.objects.none()
        self.fields['participants'].required = False

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')
        
        if date_debut and date_fin and date_debut >= date_fin:
            raise forms.ValidationError("La date de fin doit être postérieure à la date de début.")
        
        return cleaned_data