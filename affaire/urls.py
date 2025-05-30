# affaire/urls.py
from django.urls import path
from . import views

app_name = 'affaire' # Pour nommer votre application, utile pour les URLs inversées

urlpatterns = [
    path('nouvelle/', views.creer_affaire, name='nouvelle_affaire'),
    path('', views.liste_affaires, name='liste_affaires'),
    path('<int:pk>/', views.detail_affaire, name='detail_affaire'),
    path('<int:pk>/modifier/', views.modifier_affaire, name='modifier_affaire'),
]