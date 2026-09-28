from django.db import models
from .base import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from datetime import date
from fifacwc.enumerations import Companhia

class Passagem(BaseModel):
    cod_voo = models.CharField(max_length=10,
                               validators=[MinLengthValidator(1)],
                               help_text="Código do voo (ex: AA1234)")
    
    origem = models.CharField(max_length=50,
                              validators=[MinLengthValidator(3)],
                                help_text="Cidade de origem (ex: São Paulo)",
                                verbose_name="Origem")
    
    destino = models.CharField(max_length=50,
                               validators=[MinLengthValidator(3)],
                               help_text="Cidade de destino (ex: Rio de Janeiro)",
                               verbose_name="Destino")
    
    data_ida = models.DateField(validators=[MinValueValidator(date.today())],
                               help_text="Data de ida (ex: 2024-06-01)",
                               verbose_name="Partida")
    
    chegada = models.DateField(validators=[MinValueValidator(date.today())],
                                 help_text="Data e hora de chegada (ex: 2024-06-01)",
                                 verbose_name="Chegada")
    
    titular = models.CharField(max_length=150, blank=True, null=True,
                              validators=[MinLengthValidator(10)],
                              help_text="Nome do titular da passagem (ex: João Silva)",
                              verbose_name="Titular")
    
    passaporte = models.CharField(max_length=20, blank=True, null=True,
                                  help_text="Número do passaporte (ex: P1234567)",
                                  verbose_name="Passaporte",
                                  validators=[MinLengthValidator(5)])

    preco = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)],
                                help_text="Preço da passagem (ex: 1500.00)",)
    
    companhia_aerea = models.CharField(max_length=100, choices=Companhia.choices)




    class Meta:
        verbose_name_plural = "Passagens"