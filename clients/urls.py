from django.urls import path, include
from .views import (
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView
)

app_name = 'clients'

urlpatterns = [
    path('', ClientListView.as_view(), name='liste'),
    path('nouveau/', ClientCreateView.as_view(), name='creer'),
    path('<int:pk>/', ClientDetailView.as_view(), name='detail'),
    path('<int:pk>/modifier/', ClientUpdateView.as_view(), name='modifier'),
    path('<int:pk>/supprimer/', ClientDeleteView.as_view(), name='supprimer'),
    path('<int:pk>/dossiers/', include('affaire.urls')),  # Dossiers liés
]