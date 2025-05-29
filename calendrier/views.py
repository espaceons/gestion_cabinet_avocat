from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import RendezVous
from .forms import RendezVousForm
from django.utils import timezone

class CalendrierView(LoginRequiredMixin, ListView):
    model = RendezVous
    template_name = 'calendrier/liste.html'
    context_object_name = 'rendezvous'
    
    def get_queryset(self):
        return RendezVous.objects.filter(
            participants=self.request.user
        ).order_by('date_debut')

class RendezVousCreateView(LoginRequiredMixin, CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'calendrier/form.html'
    success_url = reverse_lazy('calendrier:liste')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.createur = self.request.user
        response = super().form_valid(form)
        self.object.participants.add(self.request.user)  # Ajoute le créateur comme participant
        messages.success(self.request, "Rendez-vous créé avec succès.")
        return response

class RendezVousUpdateView(LoginRequiredMixin, UpdateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'calendrier/form.html'
    success_url = reverse_lazy('calendrier:liste')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Rendez-vous mis à jour avec succès.")
        return super().form_valid(form)

class RendezVousDeleteView(LoginRequiredMixin, DeleteView):
    model = RendezVous
    template_name = 'calendrier/confirm_delete.html'
    success_url = reverse_lazy('calendrier:liste')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Rendez-vous supprimé avec succès.")
        return super().delete(request, *args, **kwargs)