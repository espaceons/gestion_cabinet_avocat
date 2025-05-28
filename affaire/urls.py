# affaire/urls.py
from django.urls import path
from . import views

app_name = 'affaire' # Pour nommer votre application, utile pour les URLs inversées

urlpatterns = [
    path('', views.liste_affaires, name='liste_affaires'),
    path('<int:pk>/', views.detail_affaire, name='detail_affaire'),
]