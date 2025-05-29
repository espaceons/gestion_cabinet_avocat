from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Document
from .forms import DocumentForm
from django.http import FileResponse

class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'dossier/document_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        return Document.objects.filter(
            affaire__avocat_responsable=self.request.user
        ).select_related('affaire')

class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'dossier/document_form.html'
    success_url = reverse_lazy('dossier:document_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        messages.success(self.request, "Document ajouté avec succès!")
        return super().form_valid(form)

class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'dossier/document_form.html'
    success_url = reverse_lazy('dossier:document_list')

    def get_queryset(self):
        return Document.objects.filter(affaire__avocat_responsable=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Document mis à jour avec succès!")
        return super().form_valid(form)

class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = 'dossier/document_confirm_delete.html'
    success_url = reverse_lazy('dossier:document_list')

    def get_queryset(self):
        return Document.objects.filter(affaire__avocat_responsable=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Document supprimé avec succès!")
        return super().delete(request, *args, **kwargs)

class DocumentDownloadView(LoginRequiredMixin, DetailView):
    model = Document

    def get(self, request, *args, **kwargs):
        document = self.get_object()
        return FileResponse(
            document.fichier.open(),
            as_attachment=True,
            filename=document.fichier.name.split('/')[-1]
        )