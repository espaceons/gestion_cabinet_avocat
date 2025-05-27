from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Facture
from .forms import FactureForm

class FactureListView(LoginRequiredMixin, ListView):
    model = Facture
    template_name = 'facturation/liste.html'
    
    def get_queryset(self):
        return Facture.objects.filter(
            affaire__avocat=self.request.user
        ).order_by('-date_emission')

class FactureCreateView(LoginRequiredMixin, CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'facturation/form.html'
    
    def get_success_url(self):
        return reverse('facturation:detail', kwargs={'pk': self.object.pk})

class FacturePDFView(LoginRequiredMixin, DetailView):
    model = Facture
    template_name = 'facturation/facture_pdf.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.affaire.avocat != request.user:
            return HttpResponseForbidden()
        
        template = get_template(self.template_name)
        html = template.render({'object': self.object})
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=facture_{self.object.numero}.pdf'
        
        pisa.CreatePDF(html, dest=response)
        return response