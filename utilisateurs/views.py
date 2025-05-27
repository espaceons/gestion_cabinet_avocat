# utilisateurs/views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import InscriptionForm

class InscriptionView(View):
    def get(self, request):
        form = InscriptionForm()
        return render(request, 'utilisateurs/inscription.html', {'form': form})

    def post(self, request):
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('utilisateurs:profil')
        return render(request, 'utilisateurs/inscription.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProfilView(View):
    def get(self, request):
        return render(request, 'utilisateurs/profil.html')


@method_decorator(login_required, name='dispatch')
class ListeUtilisateursView(View):
    def get(self, request):
        utilisateurs = User.objects.all()
        return render(request, 'utilisateurs/liste_utilisateurs.html', {'utilisateurs': utilisateurs})