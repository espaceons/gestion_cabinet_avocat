# affaire/views.py
from django.shortcuts import render, get_object_or_404
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
    documents = affaire.document_set.all().order_by('-date_upload')
    rendezvous = affaire.rendezvous_set.all().order_by('date_debut')
    factures = affaire.facture_set.all().order_by('-date_emission')

    context = {
        'affaire': affaire,
        'documents': documents,
        'rendezvous': rendezvous,
        'factures': factures,
        'titre_page': f"Détail de l'affaire : {affaire.reference}",
    }
    return render(request, 'affaire/detail_affaire.html', context)