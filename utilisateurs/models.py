from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ("AVOCAT", "Avocat"),
        ("SECRETAIRE", "Secrétaire")
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    # Solution pour les conflits de groupes et permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="utilisateur_set",  # Nom unique
        related_query_name="utilisateur",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="utilisateur_set",  # Nom unique
        related_query_name="utilisateur",
    )