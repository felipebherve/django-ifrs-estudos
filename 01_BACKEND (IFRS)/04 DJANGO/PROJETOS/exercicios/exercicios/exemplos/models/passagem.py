from exemplos.models import BaseModel, Voo

from django.db import models
from django.core.validators import MinLengthValidator
from exemplos.enumerations import Status

class Passagem(BaseModel):
    nr = models.PositiveSmallIntegerField(
        verbose_name='Número da passagem',
        help_text='Informe o número da passagem no Voo'
    )

    passageiro = models.CharField(max_length=150,
                                  validators=[MinLengthValidator(5)],
                                  help_text='Imforme o nome do passageiro.')
    
    status = models.CharField(
        max_length=20,
        help_text='Selecione o atual status da passagem',
        choices=Status,
    )

    poltrona = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
        help_text='Informe a localização da poltrona'
    )

    voo = models.ForeignKey(
        Voo,
        on_delete=models.PROTECT, 
        # CASCADE (DELETA EM FORMA DE CASCATA),
        # PROTECT (NÃO DEIXA DELETAR)
        # RESTRICT (AVISA QUE NÃO PODE)  
        # SET_NULL (SETA NULO) (MAS TEM QUE TER blank=True, Null=True)
        # SET_DEFAULT (COLOCA O DEFAULT MAS DEVE TER O DEFAULT CADASTRADO)
        verbose_name='Vôo Comercial',
        help_text='Selecione o vôo comercial',
    )

    def __str__(self):
        return f'{self.voo.cod} - {self.poltrona}: {self.passageiro} '
    
    class Meta:
        verbose_name_plural = 'Passagens'
        unique_together = [['nr', 'voo'], ['passageiro', 'voo']]