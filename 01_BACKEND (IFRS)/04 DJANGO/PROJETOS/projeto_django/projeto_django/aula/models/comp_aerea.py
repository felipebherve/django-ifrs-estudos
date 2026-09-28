from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from aula.models import BaseModel
from aula.models import Aeroporto


class CompanhiaAerea(BaseModel):

    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)],
        help_text="Informe o nome da companhia aérea."
    )

    cod = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3)],
        help_text="Informe o código com pelo menos 3 dígitos.",
        verbose_name="Código"
    )

    nr_voos = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
        verbose_name="Número de vôos",
        help_text="Informe a quantidade de vôos."
    )

    # Utilizar sempre no plural o nome da variável por ser Many To Many
    aeroportos = models.ManyToManyField(
        Aeroporto,
    )

    def __str__(self):
        return f"{self.cod}: {self.nome}"
