from django.core.validators import MinLengthValidator
from django.db import models
from aula.models import BaseModel


class Voo(BaseModel):

    cod = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        verbose_name="Vôo Comercial",
        help_text="Informe o código do vôo comercial.",
    )

    data_hora = models.DateTimeField(
        verbose_name="Data/Horário de Patida.",
        help_text="Informe a data/horario de partida.",
    )

    origem = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
        help_text="Informe o aeroporto de origem.",
    )

    destino = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
        help_text="Informe o aeroporto de destino."
    )

    def __str__(self):
        return f"Código: {self.cod} - Data/Hora: {self.data_hora} - Origem: {self.origem} - Destino: {self.destino} - {self.data_hora.strftime("%d/%m/%y - %h: %m %z")}"

    class Meta:
        verbose_name_plural = "Vôos"