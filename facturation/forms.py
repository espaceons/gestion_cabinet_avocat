# facturation/forms.py
from django import forms
from .models import Facture, Affaire # Importez également le modèle Affaire si ce n'est pas déjà fait

class FactureForm(forms.ModelForm):
    """
    Formulaire pour la création et la modification d'objets Facture.
    """
    class Meta:
        model = Facture
        fields = ['affaire', 'montant', 'date_emission', 'statut_paiement']
        # Vous pouvez exclure des champs si nécessaire, par exemple si date_emission est auto_now_add
        # exclude = ['date_creation']

        widgets = {
            'date_emission': forms.DateInput(attrs={'type': 'date'}), # Utilise un picker de date HTML5
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnalisation des labels ou ajout de placeholders
        self.fields['affaire'].label = "Affaire concernée"
        self.fields['montant'].label = "Montant de la facture (€)"
        self.fields['date_emission'].label = "Date d'émission"
        self.fields['statut_paiement'].label = "Statut du paiement"

        # Vous pouvez filtrer les choix d'affaires si nécessaire
        # Par exemple, n'afficher que les affaires "En cours"
        # self.fields['affaire'].queryset = Affaire.objects.filter(statut='EN_COURS')