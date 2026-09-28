from datetime import date

from exemplos.models import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from exemplos.enumerations import *
from exemplos.validators import ValidadorCPF
from exemplos.enumerations import Genero

class Aluno(BaseModel):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(3)],
                            default='Wellinguyngton Silva Dior',
                            verbose_name='Nome do aluno',
                            help_text='O nome deve conter pelo menos 3 caracteres.')
    
    cpf = models.CharField(max_length=14, validators=[ValidadorCPF()],
                           default='',
                           verbose_name='CPF do aluno',
                           help_text='O CPF deve ser válido e conter 11 dígitos.')
    
    email = models.EmailField(max_length=100,
                              default='',
                              verbose_name='Email do aluno',
                              help_text='Insira um email válido.')
    
    telefone = models.CharField(max_length=15, blank=True, null=True,
                                verbose_name='Telefone do aluno',
                                help_text='Insira um telefone válido com DDD.')
    
    data_nascimento = models.DateField(verbose_name='Data de nascimento do aluno',
                                       default=date.today,
                                       help_text='Insira a data de nascimento no formato YYYY-MM-DD.')
    
    genero = models.CharField(max_length=21, choices=Genero.choices,
                              default=Genero.OUTRO,
                              verbose_name='Gênero do aluno',
                              help_text='Selecione o gênero do aluno.')
    
    def __str__(self):
        return f'{self.nome} - {self.cpf}'