from rest_framework import serializers
from nlp_tasks_api.apps.text_processing.models import Documento

class DocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documento
        fields = "__all__"
