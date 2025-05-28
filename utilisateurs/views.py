# utilisateurs/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # Le formulaire de connexion par défaut de Django
from django.contrib.auth import login, logout # Les fonctions de connexion/déconnexion de Django
from django.contrib import messages # Pour afficher des messages flash (ex: succès, erreur)
from django.contrib.auth.decorators import login_required

from utilisateurs.forms import UtilisateurProfileForm


def custom_login(request):
    """
    Vue personnalisée pour la connexion des utilisateurs.
    Elle gère l'affichage du formulaire de connexion et le traitement des données soumises.
    """
    if request.method == 'POST':
        # Si la requête est de type POST, le formulaire a été soumis
        form = AuthenticationForm(request, data=request.POST) # Instancie le formulaire avec les données POST
        if form.is_valid():
            # Si les données du formulaire sont valides (nom d'utilisateur et mot de passe corrects)
            user = form.get_user() # Récupère l'objet utilisateur authentifié
            login(request, user) # Connecte l'utilisateur en créant une session
            messages.success(request, f"Bienvenue, {user.username} !") # Ajoute un message de succès

            # Redirection après connexion
            next_url = request.GET.get('next') # Vérifie si une URL de redirection est présente dans la requête (e.g. ?next=/affaires/)
            if next_url:
                return redirect(next_url) # Redirige vers l'URL d'origine demandée
            return redirect('affaire:liste_affaires') # Sinon, redirige vers une URL par défaut

        else:
            # Si le formulaire n'est pas valide (authentification échouée)
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.") # Message d'erreur
            # Le formulaire non valide sera rendu avec ses erreurs dans le template
    else:
        # Si la requête est de type GET, affiche un formulaire de connexion vide
        form = AuthenticationForm()
    
    # Rend le template de connexion avec le formulaire et le titre de la page
    return render(request, 'utilisateurs/login.html', {'form': form, 'titre_page': 'Connexion'})

def custom_logout(request):
    """
    Vue personnalisée pour la déconnexion des utilisateurs.
    """
    logout(request) # Déconnecte l'utilisateur en détruisant sa session
    messages.info(request, "Vous avez été déconnecté.") # Ajoute un message d'information
    return redirect('utilisateurs:login') # Redirige l'utilisateur vers la page de connexion (ou toute autre URL définie dans settings.py)


@login_required
def profile(request):
    """
    Vue pour afficher et modifier le profil de l'utilisateur connecté.
    """
    if request.method == 'POST':
        # Si le formulaire est soumis (POST), nous allons traiter les données
        form = UtilisateurProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour avec succès !')
            return redirect('utilisateurs:profil') # Redirige vers la même page de profil après sauvegarde
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        # Si la requête est GET, affiche le formulaire pré-rempli avec les données de l'utilisateur
        form = UtilisateurProfileForm(instance=request.user)

    context = {
        'form': form,
        'titre_page': 'Mon Profil',
        'user': request.user, # Pour afficher les infos de l'utilisateur
    }
    return render(request, 'utilisateurs/profil.html', context)