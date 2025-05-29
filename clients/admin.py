# clients/admin.py
from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_client', 'email', 'telephone', 'date_creation')
    list_filter = ('type_client',)
    search_fields = ('nom', 'email', 'telephone', 'adresse')