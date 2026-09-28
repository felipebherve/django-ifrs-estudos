from django.db import models

class Operacoes(models.TextChoices):
    #CONSTANTE = 'SIMBOLO BD', 'TEXTO_USUARIO'
    ADICAO = '+', 'Adição'
    SUBTRACAO = '-', 'Subtração'
    MULTIPLICACAO = '*', 'Multiplicação'
    DIVISAO = '/', 'Divisão'
    MODULO = '%', 'Módulo'


