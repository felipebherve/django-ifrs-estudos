from django.db import models

class Disciplinas(models.TextChoices):
    MATEMATICA = "Matemática"
    PORTUGUES = "Português"
    HISTORIA = "História"
    GEOGRAFIA = "Geografia"
    CIENCIAS = "Ciências"
    ARTES = "Artes"
    EDUCACAO_FISICA = "Educação Física"
    INFORMATICA = "Informática"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]