from django.urls import path
from .views import (
    RendezVousCreateView,
    RendezVousUpdateView,
    RendezVousDeleteView,
    CalendrierView
)

app_name = 'calendrier'

urlpatterns = [
    path('', CalendrierView.as_view(), name='liste'),
    path('nouveau/', RendezVousCreateView.as_view(), name='creer'),
    path('<int:pk>/modifier/', RendezVousUpdateView.as_view(), name='modifier'),
    path('<int:pk>/supprimer/', RendezVousDeleteView.as_view(), name='supprimer'),
]