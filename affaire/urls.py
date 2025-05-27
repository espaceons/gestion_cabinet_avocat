from django.urls import path
from .views import (
    AffaireListView,
    AffaireCreateView,
    AffaireDetailView,
    AffaireUpdateView,
    AffaireDeleteView,
    DocumentAffaireCreateView
)

app_name = 'affaires'

urlpatterns = [
    path('', AffaireListView.as_view(), name='liste'),
    path('nouvelle/', AffaireCreateView.as_view(), name='creer'),
    path('<int:pk>/', AffaireDetailView.as_view(), name='detail'),
    path('<int:pk>/modifier/', AffaireUpdateView.as_view(), name='modifier'),
    path('<int:pk>/supprimer/', AffaireDeleteView.as_view(), name='supprimer'),
    path('<int:pk>/document/', DocumentAffaireCreateView.as_view(), name='ajouter_document'),
    path('<int:pk>/calendrier/', include('calendrier.urls')),
]