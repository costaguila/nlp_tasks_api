from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User



class ListUsers(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        """
            Recebe uma requizição com n textos.
            Extrai o vocabulario, e a frequência das palavras
        """
        pass
