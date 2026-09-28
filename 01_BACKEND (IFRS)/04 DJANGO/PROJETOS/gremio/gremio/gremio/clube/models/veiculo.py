from wsgiref.validate import validator

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from clube.models import BaseModel
from django.db import models
from datetime import date
from clube.enumerations import Marca2, Cor
from clube.validators import validation_even, validation_ano_do_modelo
from django.core.exceptions import ValidationError


class Veiculo(BaseModel):
    marca = models.CharField(max_length=20, 
                             validators=[MinLengthValidator(4)],
                             choices = Marca2,
                            #   verbose_name='Qual a marca do carro?',
                            #   help_text='A marca deve conter pelomenos 2 e maximo 25 caracteres.',
                             default = Marca2.PORSCHE
                              )

    modelo = models.CharField(max_length = 25, validators=[MinLengthValidator(2),MaxLengthValidator(20)],
                              verbose_name = 'Qual o modelo do carro?',
                              help_text = 'O modelo deve conter pelo menos entre 2 e 25 caracteres.'
                              )
    
    ano =  models.IntegerField(default=0,
                               validators= [validation_ano_do_modelo],
                               verbose_name = 'Ano de fabricação.',
                               help_text = 'O ano deve ser ascima de 1900 até a data atual.'
                               )

    placa = models.CharField(max_length = 7,
                             validators = [MinLengthValidator(7), MaxLengthValidator(7)],
                             verbose_name = 'Qual a placa do carro?',
                             help_text = 'Deve conter 7 caracteres.')
    
    valor_diaria = models.IntegerField(default= 200,
                                 validators = [MinValueValidator(200)],
                                 verbose_name = 'Valor da diária',
                                 help_text='insira a diária'
                                 )
    
    seguro = models.FloatField(validators = [MinValueValidator(50)],
                                   verbose_name = 'Qual o valor do seguro do carro?',
                                   help_text = 'O seguro deve ser maior que 50.')   

    ultima_revisao =  models.DateField(validators= [MaxValueValidator(date.today)],
                               verbose_name = 'Ultima Revisão.',
                               help_text = 'A revisão não deve ter data maior que a atual.'
                               )
    
    ipva = models.BooleanField(default=False,
                               verbose_name= 'IPVA pago?',
                               help_text='Deve confirmar se o IPVA está em dia.'
    )

    alugado = models.BooleanField(default=False,
                                  verbose_name='O carro está alugado atualmente?'
    )
    
    def __str__(self):
        return f'Modelo: {self.modelo}. Marca: {self.marca} Ano: {self.ano}'

    # def save(self, *args, **kwargs):
    #     # Personalizar algo aqui

    #     super().save(*args, **kwargs)
        # print('Teste')
        # print('Teste', end='final')

    def clean(self):
        if self.marca == Marca2.PORSCHE:
            if self.valor_diaria < 2000:
                raise ValidationError({'valor_diaria': 'Para Porschea diária deve ser maior ou igual a R$ 2.000,00' })
        if self.marca == Marca2.FERRARI:
            if self.valor_diaria < 1500:
                raise ValidationError({'valor_diaria': 'Para Ferrari diária deve ser maior ou igual a R$ 1.500,00' })
        if self.marca == Marca2.FORD:
            if self.valor_diaria < 200:
                raise ValidationError({'valor_diaria': 'Para Ford diária deve ser maior ou igual a R$ 200,00' })
        if self.marca == Marca2.LARBORGHINI:
            if self.valor_diaria < 2000:
                raise ValidationError({'valor_diaria': 'Para Lamborghini diária deve ser maior ou igual a R$ 2.000,00' })
        if self.marca == Marca2.TESLA:
            if self.valor_diaria < 500:
                raise ValidationError({'valor_diaria': 'Para Tesla diária deve ser maior ou igual a R$ 2.000,00' })
        if self.marca == Marca2.BUGATTI:
            if self.valor_diaria < 5000:
                raise ValidationError({'valor_diaria': 'Para Bugatti diária deve ser maior ou igual a R$ 5.000,00' })

        if self.seguro <= 0.05*self.valor_diaria:
            # seg = self.valor_diaria * 0.05
            raise ValidationError({'seguro':f'O seguro deve ser maior que:{0.05*self.valor_diaria:0.2f}'})


        if self.alugado == True:
            if self.ipva == False:
                raise ValidationError({'alugado': 'Bloqueado para locação por falta de pagamento do IPVA'})
        # self.nota self.qualidade
        # ano: minimo -5 do atual e máximo: +1 do atual
        # seguro ascima de 50
        # revisão
        # ipva