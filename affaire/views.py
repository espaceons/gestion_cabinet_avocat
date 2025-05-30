# affaire/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from affaire.forms import AffaireForm
from .models import Affaire
from django.contrib.auth.decorators import login_required # Pour restreindre l'accès aux utilisateurs connectés

@login_required
def liste_affaires(request):
    """
    Affiche la liste de toutes les affaires.
    """
    affaires = Affaire.objects.all().select_related('client') # Optimise la requête pour récupérer aussi le client
    context = {
        'affaires': affaires,
        'titre_page': "Liste des Affaires",
    }
    return render(request, 'affaire/liste_affaires.html', context)

@login_required
def detail_affaire(request, pk):
    """
    Affiche les détails d'une affaire spécifique, ainsi que ses documents, rendez-vous et factures.
    """
    affaire = get_object_or_404(Affaire.objects.select_related('client'), pk=pk)

    # Récupérer les objets liés via les related_names (automatiquement générés par Django)
    documents = affaire.documents.all().order_by('-date_upload')
    rendezvous = affaire.rendezvous.all().order_by('date_debut')
    factures = affaire.factures.all().order_by('-date_emission')

    context = {
        'affaire': affaire,
        'documents': documents,
        'rendezvous': rendezvous,
        'factures': factures,
        'titre_page': f"Détail de l'affaire : {affaire.reference}",
    }
    return render(request, 'affaire/detail_affaire.html', context)


@login_required
def creer_affaire(request):
    if request.method == 'POST':
        form = AffaireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'affaire a été créée avec succès !')
            return redirect('affaire:liste_affaires')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = AffaireForm()
    return render(request, 'affaire/affaire_form.html', {'form': form, 'titre_page': 'Créer une Affaire'})

@login_required
def modifier_affaire(request, pk):
    affaire = get_object_or_404(Affaire, pk=pk)
    if request.method == 'POST':
        form = AffaireForm(request.POST, instance=affaire)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'affaire a été mise à jour avec succès !')
            return redirect('affaire:detail_affaire', pk=affaire.pk)
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = AffaireForm(instance=affaire)
    return render(request, 'affaires/affaire_form.html', {'form': form, 'titre_page': 'Modifier l\'Affaire'})

# Ajoutez ici des vues pour les clients, rendez-vous, documents, factures si vous les gérez dans leurs propres applications