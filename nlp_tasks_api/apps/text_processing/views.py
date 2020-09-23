from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics

from nlp_tasks_api.apps.text_processing.utils import *
from nlp_tasks_api.apps.text_processing.models import Documento
from nlp_tasks_api.apps.text_processing.serializers import DocumentoSerializer

class CountVocabularySimilarityView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        """
            Recebe uma requizição com n textos.
            Extrai o vocabulario, e a frequência das palavras

            Parâmetros:
            textos: Um array de textos.
            gram: A granularidade dos tokens.
        """
        textos = request.data.get('textos',[])
        gram = int(request.data.get('ngrams', 1))

        result = format_vocabulary_response(textos, gram)

        return Response(result, status=status.HTTP_200_OK)

class UploadFilesView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    permission_classes = (AllowAny,)

class UploadedFilesVocabularySimilarityView(generics.ListAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        textos = []
        gram = int(request.GET.get('ngrams', 1))

        for arquivo in queryset:
            with arquivo.file.open('r') as f:
                lines = f.read()
                f.close()
                lines = lines.strip()
                textos.append(lines)
        result = format_vocabulary_response(textos, gram)

        return Response(result)
