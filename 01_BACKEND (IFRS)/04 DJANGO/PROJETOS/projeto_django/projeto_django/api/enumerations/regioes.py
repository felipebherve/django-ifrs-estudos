from django.db import models

class Regioes(models.TextChoices):
    #CONSTANTE = 'SIMBOLO BD', 'TEXTO_USUARIO'
    SUL = 'SUL', 'SUL'
    SUDESTE = 'SUDESTE', 'SUDESTE'
    CENTRO_OESTE = 'CENTRO_OESTE', 'CENTRO_OESTE'
    NORTE = 'NORTE', 'NORTE'
    NORDESTE = 'NORDESTE', 'NORDESTE'

