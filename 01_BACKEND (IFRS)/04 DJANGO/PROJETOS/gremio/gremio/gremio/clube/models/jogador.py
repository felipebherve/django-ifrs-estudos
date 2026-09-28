# from wsgiref.validate import validator

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from clube.models import BaseModel
from django.db import models
from django.core.exceptions import ValidationError

class Jogador(BaseModel):
    titulo = models.CharField(max_length=100,
                              validators=[MinLengthValidator(5)],
                              verbose_name='Titulo do jogador',
                              help_text='O titulo deve conter pelomenos 5 e maximo 100'
                              )

    descricao = models.TextField(max_length= 5000,
                                 blank=True, null=True,  #deixar a variável opcional
                                 validators=[MinLengthValidator(10)],
                                 verbose_name='🧛Descrição🧛',
                                 help_text='(OPCIONAL) Informe a descrição do exemplo com no minimo 10 caracteres e maximo 5000, essa descrição ficará disponível para o usuário.')

    qualidade = models.IntegerField(default=0,
                                    validators=[MinValueValidator(0), MaxValueValidator(100)],
                                    verbose_name='Qualidade',
                                    help_text='A qualidade do exemplo deve estar entre 0 e 100'
                                    )

    nota = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                             editable = False,
                             verbose_name='Nota',
                             help_text='A nota deve estar entre 0.0 e 10.0.'
                             )
    




    def __str__(self):
        return self.titulo
    
    def clean(self):
        # self.nota self.qualidade
        if self.nota *10 < self.qualidade:
            raise ValidationError({
                'nota':'Nota e qualidade não são equivalentes', 
                'qualidade': 'Qualidade e nota não são equivalentes'
                })
        if (self.qualidade +10) / 10 > self.nota:
            raise ValidationError({
                'qualidade':'Qualidade e nota não são equivalentes',
                'nota': 'Nota e qualidade não são equivalentes'
            })
        
        if self.titulo in self.descricao:
            raise ValidationError({
                'descricao': 'A descricao não pode conter o título'
            })
        
    def save(self, *args, **kwargs):
        # Personalizar algo aqui
        self.titulo = self.titulo.title()
        if self.descricao == '' or self.descricao == None:
            self.descricao = 'Descrição não informada.'
        self.descricao = self.descricao.capitalize()

        self.nota = self.qualidade / 10

        super().save(*args, **kwargs)
        # print('Teste')
        # print('Teste', end='final')

    class Meta:
        verbose_name_plural = '🤾🏻‍♂️Jogadores🤾🏻‍♂️'





# class carro:
#     #atributos de classe
#
#     def __init__(self, modelo:str=modelo, marca:str):
#         self.modelo = modelo
#         self.marca = marca
#