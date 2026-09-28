from aula.models import BaseModel
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date, timedelta
from aula.models import Aluno
from django.core.exceptions import ValidationError


class Bolsa(BaseModel):

    # Atributos de classe
    programa = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=50,
        verbose_name="Programa",
        help_text="Digite o nome do Programa, entre 2 e 50 caracteres."
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(14000)],
        verbose_name="Valor da bolsa",
        help_text="Digite o valor da bolsa entre 0 e 14,000."
    )

    data_inicio = models.DateField(
        verbose_name="Data de Inicio",
        help_text="Selecione a data de inicio da bolsa."
    )

    data_fim = models.DateField(
        validators=[MinValueValidator(date.today)],
        verbose_name="Data de fim da Bolsa",
        help_text="Selecione a data de fim da bolsa."
    )

    aluno = models.OneToOneField(
        Aluno,
        on_delete=models.PROTECT,
        help_text="Selecione o Aluno da Bolsa."
    )

    # Métodos
    def clean(self):

        if self.data_fim >= self.data_inicio + timedelta(days=180):
            raise ValidationError({
                "data_fim": "A data de fim da bolsa deve ser no máximo a data de hoje mais 6 meses."
            })

        if self.data_fim < self.data_inicio:
            raise ValidationError({
                "data_fim": "A data de fim da bolsa deve ser maior que a data de inicio."
            })

    def __str__(self):
        return f"Nome Aluno: {self.aluno.nome} - Programa: {self.programa} - Valor: R$ {self.valor} - Data Inicio: {self.data_inicio} - Data Fim: {self.data_fim}"