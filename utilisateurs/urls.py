from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    InscriptionView,
    ProfilView,
    ListeUtilisateursView
)

app_name = 'utilisateurs'

urlpatterns = [
    # Authentification
    path('connexion/', auth_views.LoginView.as_view(
        template_name='utilisateurs/connexion.html'
    ), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='deconnexion'),
    
    # Gestion compte
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('profil/', ProfilView.as_view(), name='profil'),
    
    # Administration
    path('liste/', ListeUtilisateursView.as_view(), name='liste'),
    
    # Réinitialisation mot de passe
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='utilisateurs/password_reset.html'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='utilisateurs/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='utilisateurs/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='utilisateurs/password_reset_complete.html'
    ), name='password_reset_complete'),
]