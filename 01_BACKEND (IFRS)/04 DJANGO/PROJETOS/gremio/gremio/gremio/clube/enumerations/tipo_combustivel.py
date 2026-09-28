from django.db import models

class Tipo_combustivel(models.TextChoices):
    ELETRICO = 'Elétrico', 'Elétrico'
    HIBRIDO = 'Híbrido', 'Híbrido - Gasolina/Elétrico'
    DIESEL = 'Diesel', 'Diesel S10'
    FLEX = 'Álcool/Gasolina', 'Flex: Álcool/Gasolina'
    GASOLINA = 'Gasolina', 'Gasolina'
    ALCOOL = 'Álcool', 'Álcool'
