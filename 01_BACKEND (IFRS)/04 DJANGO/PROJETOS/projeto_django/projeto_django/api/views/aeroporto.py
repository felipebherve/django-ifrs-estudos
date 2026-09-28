from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from ..models import Aeroporto
from ..serializers import AeroportoSerializer
from rest_framework.response import Response
from rest_framework import status

class AeroportoService(APIView):
    def get(self, request, id):
        #consultar objeto #primer key
        aeroporto = get_object_or_404(Aeroporto, pk=id) #consulta se o objeto exuste
        contexto = {
            'request':request,
            'id':id,
        }
        objeto_json = AeroportoSerializer(aeroporto, context=contexto)

        return Response(objeto_json.data, status=status.HTTP_200_OK)

