from django.db import models


class Marca(models.TextChoices):
    # CONSTANTE = Valor_armazenado, Valor_usuário: O que irá aparecer para o usuário
    CHEVROLET = "Chevrolet", "Chevrolet"
    BYD = "Byd", "Build Your Dream - BYD"
    VOLKSWAGEN = "Volkswagen", "Volkswagen - VW"
    VOLVO = "Volvo", "Volvo"
    RENAULT = "Renault", "Renault"
    FIAT = "Fiat", "Fiat"
