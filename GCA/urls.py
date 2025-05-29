from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from GCA.views import DashboardView, home_view

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # Authentification
    path('utilisateurs/', include('utilisateurs.urls')),
    
    # Applications métier
    path('clients/', include('clients.urls')),
    path('affaires/', include('affaire.urls')),
    #path('rendezvous/', include('rendezvous.urls')),
    path('calendrier/', include('calendrier.urls')),
    path('facturation/', include('facturation.urls')),
    path('documents/', include('dossiers.urls')),
    
    # Page d'accueil
    #path('', TemplateView.as_view(template_name='dashboard.html'), name='home'),
    
    # API
    #path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns