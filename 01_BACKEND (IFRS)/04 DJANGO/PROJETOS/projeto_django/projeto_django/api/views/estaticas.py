from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.utils import timezone


@api_view(['GET'])
def saudacao(request, nome_pessoa='Visitante'):
    return Response(f'Olá {nome_pessoa.capitalize()}!')


@api_view(['GET'])
def numeros(request, numero= 0):
    if numero == 0:
        return Response('Zero!') 
    elif numero == 1:
            return Response('Um!') 
    elif numero == 2:
            return Response('Dois!') 
    elif numero == 3:
            return Response('Três!') 
    elif numero == 4:
            return Response('Quatro!') 
    elif numero == 5:
            return Response('Cinco!') 
    elif numero == 6:
            return Response('Seis!') 
    elif numero == 7:
            return Response('Sete!') 
    elif numero == 8:
            return Response('Oito!') 
    elif numero == 9:
            return Response('Nove!') 


class SaudacaoService(APIView):
    def get(self,request, nome_pessoa='Visitante'):
        agora = timezone.now().astimezone().hour
        if agora < 12 and agora >= 0:
            saudacao = 'Bom dia'
        elif agora >= 12 and agora <= 18:
            saudacao = 'Boa tarde'
        elif agora >= 18 and agora <= 23:
            saudacao = 'Boa noite'

        return Response(f'{saudacao.capitalize()} {nome_pessoa.capitalize()} com classe!')
    
class NumerosService(APIView):
      def get(self,request, numero=0):           
        if numero == 0:
            return Response('Zero!') 
        elif numero == 1:
                return Response('Um!') 
        elif numero == 2:
                return Response('Dois!') 
        elif numero == 3:
                return Response('Três!') 
        elif numero == 4:
                return Response('Quatro!') 
        elif numero == 5:
                return Response('Cinco!') 
        elif numero == 6:
                return Response('Seis!') 
        elif numero == 7:
                return Response('Sete!') 
        elif numero == 8:
                return Response('Oito!') 
        elif numero == 9:
                return Response('Nove!') 