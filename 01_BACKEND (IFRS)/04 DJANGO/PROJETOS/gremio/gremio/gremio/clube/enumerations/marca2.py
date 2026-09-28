from django.db import models


class Marca2(models.TextChoices):
    # CONSTANTE = valor_armazenado, valor_usuário
    PORSCHE = 'Porsche', 'Porsche'
    FERRARI = 'Ferrari', 'Ferrari'
    LARBORGHINI = "Lamborghini", 'Lamborghini'
    BUGATTI = 'Bugatti', 'Bugatti'
    FORD = 'Ford', 'Ford'
    TESLA = 'Tesla', 'Tesla'