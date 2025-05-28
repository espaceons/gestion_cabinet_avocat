from django import forms
from .models import Affaire

class AffaireForm(forms.ModelForm):
    class Meta:
        model = Affaire
        fields = ['client', 'reference', 'date_ouverture', 'statut', 'description']
        labels = {
            'client': 'Client',
            'reference': 'Référence',
            'date_ouverture': 'Date d\'ouverture',
            'statut': 'Statut',
            'description': 'Description',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la référence'}),
            'date_ouverture': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez la description'}),
        }

        def clean_reference(self):
            reference = self.cleaned_data.get('reference')
            if Affaire.objects.filter(reference=reference).exists():
                raise forms.ValidationError("Cette référence existe déjà.")
            return reference