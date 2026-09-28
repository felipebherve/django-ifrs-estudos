from django.db import models


class TipoCombustivel(models.TextChoices):
    ALCOOL = "Álcool", "Álcool"
    DIESEL = "Diesel", "Diesel"
    ELETRICO = "Elétrico", "Elétrico"
    FLEX = "Álcool/Gasolina", "Flex - Álcool/Gasolina"
    GASOLINA = "Gasolina", "Gasolina"
    HIBRIDO = "Híbrido", "Híbrido - Gasolina/Elétrico"
