from django.db import models
from api.models import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from datetime import date
from decimal import Decimal
from api.enumerations import TipoConta,TipoPessoa,Status
from django.core.exceptions import ValidationError


class Conta(BaseModel):

    favorecido = models.CharField(max_length=150,
                                  validators=[MinLengthValidator(3)],
                                  verbose_name='Favorecido',
                                  help_text='Informe o nome do favorecido.',
                                  )
    
    documento = models.CharField(max_length=14,
                                 validators=[MinLengthValidator(11)],
                                 verbose_name='CNPJ')
    
    data_vencimento = models.DateField(verbose_name='Data de Vencimento',
                                       help_text='Informe a data de vencimento')
    
    data_pagamento = models.DateField(verbose_name='Data de Pagamento',
                                       help_text='Informe a data de pagamento')
    
    valor = models.DecimalField(decimal_places=2,
                                max_digits=8,
                                help_text='Informe um valor entre R$ 0.01 e R$ 100.000,00',
                                validators=[MinValueValidator(Decimal('0.01')), MaxValueValidator(Decimal("100000.00"))],
                                verbose_name='Valor R$'
                                )
    
    tipo_pessoa = models.CharField(max_length=2,
                                   validators=[MinLengthValidator(2)],
                                   help_text='Selecione o tipo de Pessoa',
                                   choices=TipoPessoa
                                   )
    
    tipo_conta = models.CharField(max_length=10,
                                  validators=[MinLengthValidator(5)],
                                  help_text='Selecione o tipo de conta',
                                  verbose_name='Tipo de conta',
                                  choices=TipoConta)
    
    status = models.CharField(max_length=20,
                              validators=[(MinLengthValidator(3))],
                              help_text='Status da conta',
                              verbose_name='Status da cobrança',
                              choices=Status)

    def __str__(self):
        return f'{self.favorecido} : R$ {self.valor} ({self.status})'
    

    def clean(self):
        if self.data_pagamento > self.data_vencimento:
            raise ValidationError('A data de pagamento deve ser inferior ou igual a data de vencimento.')