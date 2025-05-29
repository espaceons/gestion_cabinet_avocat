from django.urls import path
from .views import (
    DocumentListView,
    DocumentCreateView,
    DocumentUpdateView,
    DocumentDeleteView,
    DocumentDownloadView
)

app_name = 'dossier'

urlpatterns = [
    path('', DocumentListView.as_view(), name='document_list'),
    path('nouveau/', DocumentCreateView.as_view(), name='document_create'),
    path('<int:pk>/modifier/', DocumentUpdateView.as_view(), name='document_update'),
    path('<int:pk>/supprimer/', DocumentDeleteView.as_view(), name='document_delete'),
    path('<int:pk>/telecharger/', DocumentDownloadView.as_view(), name='document_download'),
]