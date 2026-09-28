"""
URL configuration for projeto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import saudacao, SaudacaoService, numeros, NumerosService, LoginTesteService, NumeroTesteService, calculo, CalculoService, FreteService, AeroportoService, ContaService
from rest_framework.routers import DefaultRouter
app_name = 'api'

roteador = DefaultRouter()

roteador.register(r'conta', ContaService, 'conta')

urlpatterns = [
    path('funcao/saudacao/<str:nome_pessoa>/', saudacao, name='saudacao_funcao'),
    path('classe/saudacao/<str:nome_pessoa>/', SaudacaoService.as_view(), name='saudacao_classe'),
    
    path('funcao/numeros/<int:numero>/', numeros, name='numeros_funcao'),
    path('classe/numeros/<int:numero>/', NumerosService.as_view(), name='numeros_classe'),

    path('classe/login_teste/', LoginTesteService.as_view(), name='login_teste_classe'),
    path('classe/numero_teste/', NumeroTesteService.as_view(), name='login_teste_classe'),

    path('funcao/calculo/', calculo, name='calculo_funcao'),
    path('classe/calculo/', CalculoService.as_view(), name='calculo_classe'),

    path('calcular/frete/', FreteService.as_view(), name="frete" ),

    path('aeroporto/<int:id>/', AeroportoService.as_view(), name='aeroporto_objeto')
]

urlpatterns += roteador.urls 
