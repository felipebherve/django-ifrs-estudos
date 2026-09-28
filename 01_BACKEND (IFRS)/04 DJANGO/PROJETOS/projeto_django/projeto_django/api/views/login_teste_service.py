from rest_framework.views import APIView
from rest_framework.response import Response

class LoginTesteService(APIView):
    def get(self, request):
        usuario = request.GET.get('usuario', 'invalido')
        senha = request.GET.get('senha', 'invalido')

        if usuario == 'admin' and senha == 'admin':
            return Response('Autorizado')
        else:
            return Response('Não autorizado',status=403)
        

class NumeroTesteService(APIView):
    def get(self, request):
        numero =int(request.GET.get('numero'))
        
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


        

