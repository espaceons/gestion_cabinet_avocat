from django import forms
from .models import Document
from affaire.models import Affaire

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['affaire', 'titre', 'fichier', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'affaire': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtrer les affaires accessibles par l'utilisateur
        if user:
            self.fields['affaire'].queryset = Affaire.objects.filter(
                avocat_responsable=user
            ).order_by('-date_ouverture')

    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if fichier:
            # Limiter la taille du fichier (10MB)
            max_size = 10 * 1024 * 1024
            if fichier.size > max_size:
                raise forms.ValidationError("Le fichier ne doit pas dépasser 10MB.")
            
            # Valider les extensions
            valid_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.jpg', '.png']
            import os
            ext = os.path.splitext(fichier.name)[1]
            if ext.lower() not in valid_extensions:
                raise forms.ValidationError("Type de fichier non supporté.")
        return fichier