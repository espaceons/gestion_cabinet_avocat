# documents/admin.py
from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('titre', 'affaire', 'date_upload', 'uploader', 'fichier')
    list_filter = ('affaire', 'date_upload', 'uploader')
    search_fields = ('titre', 'description', 'affaire__reference')
    raw_id_fields = ('affaire', 'uploader')