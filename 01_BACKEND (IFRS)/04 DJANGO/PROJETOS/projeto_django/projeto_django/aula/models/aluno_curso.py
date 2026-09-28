# Sempre começar o arquivo da classe importando o BaseModel e o models.
from aula.models import BaseModel
from django.db import models
from datetime import date
# Importa todas os Validators possíveis através deste diretório.
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator, MaxValueValidator
from aula.enumerations import Curso


class AlunoCurso(BaseModel):
    nome = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
        help_text="Insira o nome completo do aluno entre 5 e 200 caracteres."
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        help_text="Selecione a data de nascimento do aluno.",
        #todo : Fazer a validação para menores de idade.
        validators=[MaxValueValidator(date.today)]
    )

    cpf = models.CharField(
        max_length=14,
        validators=[RegexValidator(
            regex=r"^\d{3}.\d{3}.\d{3}-\d{2}$",
            message="Informe o CPF no formato XXX.XXX.XXX-XX")],
        help_text="Informe o número de CPF do aluno."
    )

    curso = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(3)],
        help_text="Selecione o curso do aluno entre as opções possíveis.",
        choices=Curso,
    )

    def __str__(self) -> str:
        return f"{self.nome} - ({self.curso})"
