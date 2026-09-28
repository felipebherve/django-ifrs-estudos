from exemplos.models import BaseModel
from django.db import models

from django.core.validators import MinLengthValidator


class Voo(BaseModel):

    cod = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        verbose_name='Código do Vôo:',
        help_text='Qual o código do vôo?'
    )

    data_horario = models.DateTimeField(
                                   verbose_name='Data e hora da partida.',
                                   help_text='Escolha a data e hora da partida.',                                   
                                   )
    
    origem = models.CharField(max_length=3,
                               validators=[MinLengthValidator(3)],
                               help_text='Informe a origem do vôo')
    
    destino = models.CharField(max_length=3,
                               validators=[MinLengthValidator(3)],
                               help_text='Informe o destino do vôo')

    def __str__(self):
        return f' Código {self.cod} - Data: {self.data_horario} [{self.origem} --> {self.destino}] {self.data_horario.strftime("%d/%m/%Y - %H:%m %Z")}'
    
    class Meta:
        verbose_name_plural = 'Vôos'    