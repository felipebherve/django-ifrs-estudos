from django.contrib import admin
from django.db import models
from exemplos.models import BaseModel
from django.core.validators import MinLengthValidator

class Aeroporto(BaseModel):
    cod = models.CharField(
        max_length= 3,
        validators=[MinLengthValidator(3)],
        verbose_name='Código Grêmionacional',
        help_text='Informe o código da companhia'
    )

    cidade = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        help_text='Informe a cidade do aeroporto',
    )

    pais = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        verbose_name='País',
        help_text='Informe o país do aeroporto.'
    )

    def __str__(self):
        return f'{self.cod} - {self.pais}'
    
class AeroportoAdmin(admin.ModelAdmin):
    list_display = ('cod', 'cidade', 'pais')
    search_fields = ('pais', 'cod')
    list_filther = ('cidade')