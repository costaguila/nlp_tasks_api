from django.contrib import admin
from nlp_tasks_api.apps.text_processing.models import Documento

class DocumentoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('created_at', 'file')


admin.site.register(Documento, DocumentoAdmin)
