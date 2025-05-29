from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/liste_clients.html'
    context_object_name = 'clients'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtre par recherche
        if search := self.request.GET.get('search'):
            queryset = queryset.filter(nom__icontains=search)
        return queryset.order_by('nom')

class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/form.html'
    success_url = reverse_lazy('clients:liste')
    permission_required = 'clients.add_client'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/detail_client.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['affaires'] = self.object.affaire_set.all()
        return context

class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/form.html'
    success_url = reverse_lazy('clients:liste')
    permission_required = 'clients.change_client'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user  # Optionnel : en supposant que vous ayez un champ 'modified_by'
        return super().form_valid(form)

class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/confirm_delete.html'
    success_url = reverse_lazy('clients:liste')
    permission_required = 'clients.delete_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.object  # Pour afficher le client que vous allez supprimer
        return context