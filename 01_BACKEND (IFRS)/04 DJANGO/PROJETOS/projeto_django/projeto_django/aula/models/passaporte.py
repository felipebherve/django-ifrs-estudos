from django.db import models
from aula.models import BaseModel, Pessoa
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from datetime import date, timedelta



class Passaporte(BaseModel):

    numero = models.CharField(
        max_length=7,
        validators=[MinLengthValidator(7)],
        verbose_name="Número do Passaporte",
        help_text="Insira o código alfanumérico do passaporte."
    )

    data_expedicao = models.DateField(
        validators=[MaxValueValidator(date.today)],
        verbose_name="Data de Expedição",
        help_text="Selecione a data de expedição do passaporte."
    )

    data_validade = models.DateField(
        validators=[MinValueValidator(date.today)],
        editable=False,
        verbose_name="Data de validade",
        help_text="Selecione a data de validade do passaporte."
    )

    pessoa = models.OneToOneField(
        Pessoa, null=True, blank=True,
        on_delete=models.PROTECT,
        help_text="Selecione o titular do Passaporte."
    )

    # Métodos
    def save(self, *args, **kwargs):
        self.data_validade = self.data_expedicao + timedelta(days=3650)
        super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.numero} -> {self.data_validade}"
