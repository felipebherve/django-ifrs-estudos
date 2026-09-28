from django.db import models
from aula.models import BaseModel
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

class Aluno(BaseModel):

    # Atributos de classe
    nome = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=120,
        verbose_name="Nome do Aluno",
        help_text="Digite o Nome do Aluno, entre 2 e 120 caracteres."
    )

    cidade = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=70,
        verbose_name="Cidade do Aluno",
        help_text="Digite a cidade do aluno, entre 2 e 70 caracteres."
    )

    universidade = models.CharField(
        validators=[MinLengthValidator(4)],
        max_length=20,
        verbose_name="Universidade do Aluno",
        help_text="Digite a Universidade do Aluno, entre 4 e 20 caracteres."
    )



    def __str__(self):
        return f"{self.nome} - {self.cidade} - {self.universidade}"