from django.db import models


class Curso(models.TextChoices):

    MEDICINA = "Medicina", "Medicina"
    PROGRAMACAO = "Programação", "Programação"
    ENGENHARIA = "Engenharia da Computação", "Engenharia da Computação"
    LETRAS = "Letras", "Letras"
    MATEMATICA = "Matematica", "Matemática"
    FISICA = "Fisica", "Física"
    INFORMATICA = "Informática", "Informática"
    CIENCIA_COMPUTACAO = "Ciência da Computação", "Ciência da Computação"
