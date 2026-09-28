from django.db import models


class Marca(models.TextChoices):
    # CONSTANTE = valor_armazenado, valor_usuário
    CHEVROLET = 'Chevrolet', 'Chevrolet'
    BYD = 'Byd', 'Build Your Dreams - BYD'
    VOLKSWAGEN = 'Volkswagen', 'Volkswagen - VM'
    VOLVO = 'Volvo', 'Volvo'
    RENAULT = 'Renault', 'Renault'
    FIAT = 'Fiat', 'Fiat'
