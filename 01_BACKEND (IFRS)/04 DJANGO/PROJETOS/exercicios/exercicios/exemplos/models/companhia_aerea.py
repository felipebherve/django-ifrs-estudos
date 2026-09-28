from django.db import models
from exemplos.models import BaseModel, Aeroporto
from django.core.validators import MinLengthValidator, MinValueValidator

class CompanhiaAerea(BaseModel):

    nome = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)],
        help_text='Digite o nome da CIA Aérea.'
    )

    cod = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3)],
        verbose_name='Código da CIA',
        help_text='Informe o código entre 3 a 20 digitos',
    )

    nr_voos = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
        verbose_name='Número de Vôos',
        help_text='Informe a quantidade de vôos',
    )

    aeroportos = models.ManyToManyField(
        Aeroporto

    )


    def __str__(self):
        return f'{self.cod}: {self.nome}'


