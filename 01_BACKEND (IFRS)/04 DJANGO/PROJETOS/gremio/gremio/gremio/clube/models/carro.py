from wsgiref.validate import validator

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from clube.models import BaseModel
from django.db import models
from datetime import date
from clube.enumerations import Marca, Cor
from clube.validators import validation_even, PalavrasProibidas
from clube.validators.code import CodeValidator


class Carro(BaseModel):
    marca = models.CharField(max_length=25, 
                             validators=[MinLengthValidator(2)],
                             choices = Marca,
                            #   verbose_name='Qual a marca do carro?',
                            #   help_text='A marca deve conter pelomenos 2 e maximo 25 caracteres.',
                             default = Marca.BYD
                              )

    modelo = models.CharField(max_length = 25, validators=[MinLengthValidator(2), PalavrasProibidas(['Inter', 'Colorado'])],
                              verbose_name = 'Qual o modelo do carro?',
                              help_text = 'O modelo deve conter pelo menos entre 2 e 25 caracteres.'
                              )

    ano =  models.IntegerField(default=0,
                               validators= [MaxValueValidator(date.today().year), MinValueValidator(1900)],
                               verbose_name = 'Ano de fabricação.',
                               help_text = 'O ano deve ser ascima de 1900 até a data atual.'
                               )

    placa = models.CharField(max_length = 8,
                             validators = [MinLengthValidator(8), MaxLengthValidator(8)],
                             verbose_name = 'Qual a placa do carro?',
                             help_text = 'Deve conter 8 caracteres.')

    chassi = models.CharField(max_length = 13,
                              validators = [MinLengthValidator(13), MaxLengthValidator(13)],
                              verbose_name = 'Qual o chassi do carro?',
                              help_text = 'O chassi deve ter exatamente 13 caracteres.'
                              )

    cor = models.IntegerField(choices = Cor,
                              default = Cor.AZUL,
                              verbose_name = 'Qual a cor do carro?',
                        #    help_text = 'A cor deve ter no mínimo 4 caracteres e no máximo 20'
                           )

    cor_lateral = models.CharField(max_length=20,
                           validators=[MinLengthValidator(4), MaxLengthValidator(20)],
                           verbose_name='Qual a cor lateral do carro?',
                           help_text='A cor deve ter no mínimo 4 caracteres e no máximo 20'
                           )

    velocidade = models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(500)],
                                   verbose_name = 'Qual a velocidade máxima do carro?',
                                   help_text = 'A velocidade deve ser maior que zero e menor que 500.')

    tipo_combustivel = models.CharField(max_length = 15,
                                        validators = [MinLengthValidator(2), MaxLengthValidator(15)],
                                        verbose_name = 'Qual tipo de combustível ele usa?',
                                        help_text = 'Deve ter entre 2 e 15 caracteres.')

    numeros_pares = models.IntegerField(default = 0,
                                        verbose_name = 'Número',
                                        validators = [validation_even, CodeValidator(200)],
                                        help_text = 'Insira o seu número escolhido. Lembre-se que apenas são aceitos números pares e únicos.',
                                        unique = True
                                        )
    
    codigo = models.IntegerField(blank=True, null=True,
                                 validators = [CodeValidator(100)],
                                 verbose_name = 'Código',
                                 help_text='insira o código'
                                 )


    def __str__(self):
        return (f'Marca: {self.marca}'
                f'Modelo: {self.modelo}'
                f'Ano: {self.ano}'
                f'Placa {self.placa}'
                f'Chassi: {self.chassi}'
                f'Cor: {self.cor}'
                f'Cor-lateral: {self.cor_lateral}'
                f'Velocidade: {self.velocidade}'
                f'Tipo de Combustivel: {self.tipo_combustivel}')


    class Meta:
        verbose_name_plural = '🚗Carros️🚗'