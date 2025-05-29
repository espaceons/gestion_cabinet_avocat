
# facturation/views.py
from django.views.generic import DetailView # Pour afficher les détails d'un objet
from django.http import HttpResponse
from django.template.loader import render_to_string # Pour charger le template HTML
from GCA import settings

from django.contrib.auth.mixins import LoginRequiredMixin # Pour protéger la vue
# facturation/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Facture, Affaire # Assurez-vous d'importer vos modèles
from .forms import FactureForm # Importez votre FactureForm






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