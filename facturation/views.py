
# facturation/views.py
from django.views.generic import DetailView # Pour afficher les détails d'un objet
from django.http import HttpResponse
from django.template.loader import render_to_string # Pour charger le template HTML
from GCA import settings
from weasyprint import HTML, CSS # Importez WeasyPrint
from django.contrib.auth.mixins import LoginRequiredMixin # Pour protéger la vue
# facturation/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Facture, Affaire # Assurez-vous d'importer vos modèles
from .forms import FactureForm # Importez votre FactureForm


class FacturePDFView(WeasyTemplateResponseMixin, DetailView):
    """
    Génère une facture PDF à partir d'un template Django.
    """
    model = Facture
    template_name = 'facturation/facture_pdf.html' # Le template HTML qui sera converti en PDF
    
    # Nom du fichier PDF de sortie. Utilisez des variables du contexte si besoin.
    # On utilise 'filename' au lieu de 'pdf_filename' pour le mixin plus récent de django-weasyprint
    pdf_attachment = True # Définit si le fichier doit être téléchargé (True) ou affiché dans le navigateur (False)
    
    def get_filename(self):
        """
        Définit le nom du fichier PDF à télécharger.
        """
        # Récupère l'objet facture actuel pour nommer le fichier
        facture = self.get_object()
        return f"facture_{facture.pk}_{facture.date_emission|date:'Ymd'}.pdf"

    def get_context_data(self, **kwargs):
        """
        Ajoute des données supplémentaires au contexte du template si nécessaire.
        """
        context = super().get_context_data(**kwargs)
        # Vous pouvez ajouter ici des informations sur votre cabinet par exemple
        context['cabinet_nom'] = "Cabinet Avocats ABC"
        context['cabinet_adresse'] = "123 Rue de la Justice, 75001 Paris"
        context['cabinet_telephone'] = "01 23 45 67 89"
        context['cabinet_email'] = "contact@cabinetabc.com"
        
        # Pour les images et les styles dans le PDF, il est crucial d'avoir des chemins absolus
        # WeasyPrint gère généralement bien les chemins relatifs si STATIC_URL est configuré,
        # mais pour plus de robustesse, surtout pour les logos, un chemin absolu est recommandé.
        # Vous devrez vous assurer que votre logo est dans votre dossier staticfiles
        # par exemple: static/img/logo.png
        context['logo_path'] = f"{settings.STATIC_ROOT}/img/logo.png" # Chemin absolu vers le logo si utilisé
        # Ou si vous utilisez STATIC_URL et que WeasyPrint le gère:
        # context['logo_url'] = settings.STATIC_URL + 'img/logo.png' 
        
        return context



@login_required
def creer_facture(request):
    """
    Vue pour créer une nouvelle facture.
    """
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La facture a été créée avec succès !')
            return redirect('facturation:liste_factures') # Redirige vers la liste des factures
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = FactureForm() # Formulaire vide pour une requête GET

    context = {
        'form': form,
        'titre_page': 'Créer une nouvelle facture',
    }
    return render(request, 'facturation/facture_form.html', context)

@login_required
def modifier_facture(request, pk):
    """
    Vue pour modifier une facture existante.
    """
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            messages.success(request, 'La facture a été mise à jour avec succès !')
            return redirect('facturation:liste_factures') # Redirige vers la liste
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = FactureForm(instance=facture) # Formulaire pré-rempli pour la modification

    context = {
        'form': form,
        'titre_page': 'Modifier la facture',
    }
    return render(request, 'facturation/facture_form.html', context)

# N'oubliez pas votre liste_factures que vous avez déjà demandée
@login_required
def liste_factures(request):
    factures = Facture.objects.all().select_related('affaire')
    context = {
        'factures': factures,
        'titre_page': 'Liste des Factures',
    }
    return render(request, 'facturation/liste_factures.html', context)



@login_required
class FactureDetailView(DetailView):
    """
    Vue pour afficher les détails d'une facture spécifique.
    """
    model = Facture
    template_name = 'facturation/facture_detail.html'
    context_object_name = 'facture' # Le nom de la variable utilisée dans le template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = f"Détails de la Facture #{self.object.pk}"
        # Vous pouvez ajouter ici d'autres données au contexte si nécessaire,
        # par exemple des objets liés à la facture (lignes de facture si vous les avez).
        return context