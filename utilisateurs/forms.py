# utilisateurs/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from utilisateurs.models import Utilisateur

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class UtilisateurProfileForm(forms.ModelForm):
    """
    Formulaire pour permettre aux utilisateurs de modifier leurs propres informations de profil.
    Il exclut les champs sensibles comme le mot de passe, les permissions ou le rôle (qui devrait être géré par un admin).
    """
    class Meta:
        model = Utilisateur
        # Champs que l'utilisateur peut modifier via son profil
        fields = ['first_name', 'last_name', 'email']
        # Vous pouvez ajouter d'autres champs de votre modèle Utilisateur si vous le souhaitez,
        # par exemple 'telephone', 'adresse' si vous les avez ajoutés à votre Utilisateur.
        # Excluez les champs sensibles ou gérés par l'administration uniquement
        exclude = ['password', 'last_login', 'is_superuser', 'groups',
                   'user_permissions', 'is_staff', 'is_active', 'date_joined', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnalisation des labels ou ajout de placeholders si désiré
        self.fields['first_name'].label = "Prénom"
        self.fields['last_name'].label = "Nom de famille"
        self.fields['email'].label = "Adresse e-mail"
        
        # Exemple d'ajout d'attributs HTML (placeholders)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Votre prénom'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Votre nom'})
        self.fields['email'].widget.attrs.update({'placeholder': 'votre.email@example.com'})