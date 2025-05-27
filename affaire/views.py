from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone
from .models import Affaire, Dossier
from .forms import AffaireForm, DossierForm

class AffaireListView(LoginRequiredMixin, ListView):
    model = Affaire
    template_name = 'affaires/liste.html'
    paginate_by = 15
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtres avancés
        statut = self.request.GET.get('statut')
        if statut:
            queryset = queryset.filter(statut=statut)
            
        # Recherche
        if search := self.request.GET.get('search'):
            queryset = queryset.filter(
                Q(reference__icontains=search) |
                Q(client__nom__icontains=search) |
                Q(description__icontains=search)
            )
            
        # Tri par urgence
        return queryset.order_by('-date_limite', 'statut')

class AffaireCreateView(LoginRequiredMixin, CreateView):
    model = Affaire
    form_class = AffaireForm
    template_name = 'affaires/form.html'
    
    def get_success_url(self):
        return reverse('affaires:detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.avocat = self.request.user
        return super().form_valid(form)

class AffaireDetailView(LoginRequiredMixin, DetailView):
    model = Affaire
    template_name = 'affaires/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = self.object.document_set.all()
        context['dossiers'] = self.object.dossier_set.all()
        context['now'] = timezone.now()
        return