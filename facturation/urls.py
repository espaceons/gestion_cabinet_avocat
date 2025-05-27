from django.urls import path
from .views import (
    FactureListView,
    FactureCreateView,
    FactureDetailView,
    FacturePDFView,
    PaiementCreateView
)

app_name = 'facturation'

urlpatterns = [
    path('', FactureListView.as_view(), name='liste'),
    path('nouvelle/', FactureCreateView.as_view(), name='creer'),
    path('<int:pk>/', FactureDetailView.as_view(), name='detail'),
    path('<int:pk>/pdf/', FacturePDFView.as_view(), name='pdf'),
    path('<int:pk>/paiement/', PaiementCreateView.as_view(), name='paiement'),
]