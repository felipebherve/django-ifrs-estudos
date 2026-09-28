from django.db import models

class Cor(models.IntegerChoices):
    AZUL = 1, "Azul"
    PRETO = 2, "Preto"
    BRANCO = 3, "Branco"
    AMARELO = 4, "Amarelo"
    ROXO = 5, "Roxo"
