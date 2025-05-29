# utilisateurs/forms.py
from django import forms
from .models import Utilisateur

class UtilisateurProfileForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['first_name', 'last_name', 'email', 'telephone', 'adresse']
        exclude = ['password', 'last_login', 'is_superuser', 'groups',
                   'user_permissions', 'is_staff', 'is_active', 'date_joined', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Prénom"
        self.fields['last_name'].label = "Nom de famille"
        self.fields['email'].label = "Adresse e-mail"
        self.fields['telephone'].label = "Téléphone"
        self.fields['adresse'].label = "Adresse"
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Votre prénom'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Votre nom'})
        self.fields['email'].widget.attrs.update({'placeholder': 'votre.email@example.com'})