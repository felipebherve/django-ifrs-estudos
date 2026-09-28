from aula.models import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from datetime import date

class Pessoa(BaseModel):
    # Atributos da classe de pessoa.
    nome = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2)],
        help_text="Insira o nome completo."
    )

    data_nascimento = models.DateField(
        validators=[MaxValueValidator(date.today)],
        verbose_name="Data de nascimento",
        help_text="Selecione a data de nascimento."
    )

    cpf = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        help_text="Digite somente os números do CPF."
    )

    def __str__(self):
        return f"{self.nome} ({self.cpf})"