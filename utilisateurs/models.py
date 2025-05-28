# utilisateurs/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Utilisateur(AbstractUser):
    """
    Modèle d'utilisateur personnalisé pour l'application de gestion de cabinet d'avocats.
    Hérite de AbstractUser de Django pour inclure les champs d'authentification de base
    (username, password, email, first_name, last_name, is_active, is_staff, is_superuser, last_login, date_joined).
    """
    ROLE_CHOICES = [
        ("AVOCAT", "Avocat"),
        ("SECRETAIRE", "Secrétaire")
    ]
    role = models.CharField( max_length=20, choices=ROLE_CHOICES, default="SECRETAIRE", # Rôle par défaut si non spécifié
        verbose_name="Rôle",
        help_text="Le rôle de l'utilisateur au sein du cabinet (Avocat ou Secrétaire)."
    )

    # Solution pour les conflits de groupes et permissions de Django si vous avez plusieurs modèles d'utilisateur
    # liés à AbstractUser ou si vous rencontrez des erreurs de migration.
    # Ces related_name garantissent l'unicité.
    groups = models.ManyToManyField( Group, verbose_name='groupes', blank=True, help_text='Les groupes auxquels cet utilisateur appartient. Un utilisateur '
                  'obtiendra toutes les permissions accordées à chacun de ses groupes.',
        related_name="utilisateur_set",  # Nom unique pour éviter les conflits
        related_query_name="utilisateur",
    )
    user_permissions = models.ManyToManyField( Permission, verbose_name='permissions utilisateur', blank=True, help_text='Permissions spécifiques pour cet utilisateur.',
        related_name="utilisateur_set",  # Nom unique pour éviter les conflits
        related_query_name="utilisateur",
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['username'] # Tri par nom d'utilisateur par défaut

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'utilisateur.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} ({self.get_role_display()})"
        return f"{self.username} ({self.get_role_display()})"

    def get_full_name(self):
        """
        Retourne le nom complet de l'utilisateur.
        """
        return super().get_full_name() # Utilise la méthode de AbstractUser

    def get_short_name(self):
        """
        Retourne le prénom de l'utilisateur.
        """
        return super().get_short_name() # Utilise la méthode de AbstractUser

    # Vous pouvez ajouter ici des méthodes personnalisées, par exemple :
    def is_avocat(self):
        """Vérifie si l'utilisateur a le rôle d'Avocat."""
        return self.role == "AVOCAT"

    def is_secretaire(self):
        """Vérifie si l'utilisateur a le rôle de Secrétaire."""
        return self.role == "SECRETAIRE"