from django.db import models


class Marcas_Veiculo(models.TextChoices):

    # CONSTANTE = Valor_armazenado, Valor_usuário: O que irá aparecer para o usuário
    PORSCHE = "Porsche", "Porsche"
    FERRARI = "Ferrari", "Ferrari"
    FORD = "Ford", "Ford"
    LAMBORGHINI = "Lamborghini", "Lamborghini"
    TESLA = "Tesla", "Tesla"
    BUGATTI = "Bugatti", "Bugatti"

