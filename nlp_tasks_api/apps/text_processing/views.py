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
        gram = request.data.get('ngrams', 1)

        textos_1 = [ strip_punctuation(texto_1.lower().strip()) for texto_1 in textos]
        tokens_text1 = [texto.split(' ') for texto in textos_1]
        ngrams_text1 = [n_gram(tokens, gram) for tokens in tokens_text1]

        flat = [item for sublist in ngrams_text1 for item in sublist]
        vocabulario = unique(flat)

        occurrance_list1 = [count_ocurrance(ngrams_text, vocabulario) for ngrams_text in ngrams_text1]

        response = []
        for index, item in enumerate(textos):
            response.append({
                "texto": item,
                "n_gram": gram,
                "tokens": tokens_text1[index],
                "ngrams_texto": ngrams_text1[index],
                "ocurrence": occurrance_list1[index]
            })
        result = {
            "vocabulario": vocabulario,
            "resultados": response
        }


        return Response(result, status=status.HTTP_200_OK)

class UploadFilesView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    permission_classes = (AllowAny,)

class UploadedFilesVocabularySimilarityView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    permission_classes = (AllowAny,)
