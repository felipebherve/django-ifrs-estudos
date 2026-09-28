from django.db import models
from .base import BaseModel
from fifacwc.models import Ingresso, Passagem
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from fifacwc.enumerations import Pagamento

class Pacote(BaseModel):
    nome_responsavel = models.CharField(max_length=150,
                                        validators=[MinLengthValidator(10)],)
    
    email = models.EmailField(max_length=254, validators=[MinLengthValidator(10)],
                              help_text="Email do responsável pelo pacote (ex:'nome@exemplo.com)")
    
    data_compra = models.DateField(validators=[MinValueValidator(date.today())],
                                   help_text="Data da compra do pacote (ex: 2024-06-01)",
                                   verbose_name="Data da Compra")
    
    preco_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      validators=[MinValueValidator(0)],
                                      help_text="Preço total do pacote (ex: 1000.00)",
                                      verbose_name="Preço Total")
    
    pagamento = models.CharField(max_length=50, choices=Pagamento.choices,
                                 help_text="Forma de pagamento do pacote (ex: CC - Cartão de Crédito)",
                                 verbose_name="Pagamento")
    
    ingressos = models.ForeignKey(
        Ingresso,
          on_delete=models.PROTECT,
          help_text="Selecione o ingresso do pacote",
          verbose_name="Ingresso")
    
    passagens = models.ForeignKey(
        Passagem,
          on_delete=models.PROTECT,
          help_text="Selecione a passagem do pacote",
          verbose_name="Passagem")

    
    def __str__(self):
        return f'{self.nome_responsavel} - {self.data_compra}'