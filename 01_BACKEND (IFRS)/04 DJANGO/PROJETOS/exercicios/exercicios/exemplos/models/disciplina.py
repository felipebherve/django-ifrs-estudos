from exemplos.models import BaseModel
from exemplos.enumerations import Disciplinas
from django.db import models
from django.core.validators import MinLengthValidator
from exemplos.enumerations import *

class Disciplina(BaseModel):
    nome = models.CharField(max_length=100, choices=Disciplinas.choices,
                            default=Disciplinas.MATEMATICA,
                            verbose_name='Nome da disciplina',
                            help_text='Selecione a disciplina.')
    
    def __str__(self):
        return f'{self.nome}'