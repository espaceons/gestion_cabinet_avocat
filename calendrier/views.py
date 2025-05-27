from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from .models import RendezVous
from .forms import RendezVousForm

class CalendrierView(LoginRequiredMixin, ListView):
    model = RendezVous
    template_name = 'calendrier/calendrier.html'
    
    def get_queryset(self):
        return RendezVous.objects.filter(
            participants=self.request.user,
            date_debut__gte=timezone.now()
        ).order_by('date_debut')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RendezVousCreateView(LoginRequiredMixin, CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'calendrier/form.html'
    
    def get_success_url(self):
        return reverse('calendrier:vue_calendrier')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.participants.add(self.request.user)
        return response