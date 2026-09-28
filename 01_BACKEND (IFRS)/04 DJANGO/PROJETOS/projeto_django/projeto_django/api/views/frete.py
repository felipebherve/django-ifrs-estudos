from rest_framework.parsers import JSONParser
from api.serializers.frete import FreteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView





class FreteService(APIView):
    def get(self, request):
        serializador = FreteSerializer()
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request):
            try:
                dados = request.data 
                serializador = FreteSerializer(data=dados)
                if serializador.is_valid():
                    serializador.calcular()
                    return Response(serializador.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)
            except Exception as erro:
                    contexto = {
                        'error':str(erro)
                    }
                    return Response(contexto, status=status.HTTP_400_BAD_REQUEST)