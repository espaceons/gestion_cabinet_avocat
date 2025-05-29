from django.urls import path

from . import views
app_name = 'facturation'

urlpatterns = [
    
    path('', views.liste_factures, name='liste_factures'),
    path('creer/', views.creer_facture, name='creer_facture'),
    path('modifier/<int:pk>/', views.modifier_facture, name='modifier_facture'),
    # URL pour afficher les détails d'une facture
    path('<int:pk>/', views.FactureDetailView, name='detail_facture'), # Utilisez le PK pour identifier la facture
]