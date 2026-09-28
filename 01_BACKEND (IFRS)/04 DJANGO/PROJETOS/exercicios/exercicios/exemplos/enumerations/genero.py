from django.db import models

class Genero(models.TextChoices):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    TRANSMASC = "Transgênero Masculino"
    TRANSFEM = "Transgênero Feminino"
    OUTRO = "Outro"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]