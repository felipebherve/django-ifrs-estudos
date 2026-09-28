from django.db import models
from .base import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from fifacwc.enumerations import Fase, Setor
from datetime import date

class Ingresso(BaseModel):

    titular = models.CharField(max_length=150,
                              validators=[MinLengthValidator(10)],
                              help_text="Nome do titular do ingresso (ex: João Silva)",
                              verbose_name="Titular")
    
    passaporte = models.CharField(max_length=20, blank=True, null=True,
                                  help_text="Número do passaporte (ex: P1234567)",
                                  verbose_name="Passaporte",
                                  validators=[MinLengthValidator(5)])
    
    data_compra = models.DateField(validators=[MinValueValidator(date.today())], blank=True, null=True, 
                                   help_text="Data da compra do ingresso (ex: 2024-06-01)",
                                   verbose_name="Data da Compra")
    
    preco = models.DecimalField(max_digits=10, decimal_places=2,
                            validators=[MinValueValidator(0)],
                            help_text="Preço do ingresso (ex: 500.00)",
                            verbose_name="Preço")
    
    estadio = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            help_text="Nome do estádio (ex: Estádio do Maracanã)",
                            verbose_name="Estádio")

    setor = models.CharField(max_length=50, choices=Setor.choices,
                             help_text="Setor do ingresso (ex: VIP - Área VIP)",
                             verbose_name="Setor")
    
    data_jogo = models.DateField(validators=[MinValueValidator(date.today())],
                              help_text="Data do jogo (ex: 2024-06-01)",
                              verbose_name="Data do Jogo")

    fase = models.CharField(max_length=50, choices=Fase.choices,
                            help_text="Fase do jogo (ex: GR - Grupo)",
                            verbose_name="Fase")
    
    cidade = models.CharField(max_length=100,
                            validators=[MinLengthValidator(2)],
                            help_text="Cidade do jogo (ex: Rio de Janeiro)",
                            verbose_name="Cidade")
    
    
    
    def __str__(self):
        return f'{self.titular} - {self.setor} - {self.preco}'
