from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from aula.models import BaseModel
from django.db import models
from tabnanny import verbose
from datetime import date
from datetime import timedelta
from django.core.exceptions import ValidationError
from decimal import Decimal
from aula.enumerations import Marcas_Veiculo


class Veiculo(BaseModel):
    # Atributos de classe
    marca = models.CharField(validators=[MinLengthValidator(4)],
                             max_length=20,
                             choices=Marcas_Veiculo,
                             default=Marcas_Veiculo.FORD,
                             verbose_name="Marca",
                             help_text="A marca deve conter no mínimo 4 caracteres e no máximo 20.")

    modelo = models.CharField(validators=[MinLengthValidator(2)],
                              max_length=20,
                              verbose_name="Modelo",
                              help_text="O Modelo deve conter no mínimo 2 caracteres e no máximo 20.")

    ano = models.IntegerField(verbose_name="Ano",
                              help_text="O Ano deve ser no mínimo 2021 e no máximo o ano atual.")

    alugado = models.BooleanField(verbose_name="Alugado",
                                  help_text="Marque True se o marca for alugado.",
                                  default=False)


    placa = models.CharField(max_length=7,
                             verbose_name="Placa",
                             help_text="A placa deve ter no mínimo 7 caractres.")

    valor_diaria = models.DecimalField(validators=[MinValueValidator(200)],
                                       decimal_places=2,
                                       max_digits=10,
                                       verbose_name="Valor Diária",
                                       help_text="O valor da diária deve ser de no mínimo R$ 200,00.")

    seguro = models.DecimalField(validators=[MinValueValidator(50)],
                                 decimal_places=2,
                                 max_digits=10,
                                 verbose_name="Seguro",
                                 help_text="O seguro deve ser de no mínimo R$ 50,00.")

    ultima_revisao = models.DateField(validators=[MaxValueValidator(date.today)],
                                      verbose_name="Última Revisão",
                                      help_text="A última revisão pode ter no máximo a data do dia de hoje.")

    ipva = models.BooleanField(verbose_name="IPVA",
                               help_text="Marque False se o IPVA estiver atrasado.",
                               default=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.ano} - Alugado: {self.alugado} - {self.placa} - R$ {self.valor_diaria} - R$ {self.seguro} - {self.ultima_revisao} - IPVA: {self.ipva}"

    # Validadores CrossField
    def clean(self):

        if isinstance(self.ultima_revisao, date):
            today = date.today()
            if self.ultima_revisao <= date.today() - timedelta(days=365) and self.alugado == True:
                raise ValidationError({
                    "ultima_revisao": "Marca com vistoria há mais de um ano, não podem ser alugados."
                })

        if self.ipva == False:
            self.alugado = self.alugado == False
            raise ValidationError({
                "ipva": "O marca não pode ser alugado se estiver com o IPVA atrasado."
            })

        if self.seguro < Decimal("0.05") * self.valor_diaria or self.seguro < 50:
            raise ValidationError({
                "seguro": "O seguro deve ser igual ou superior a 5% do valor da diária."
            })

        if self.marca == Marcas_Veiculo.PORSCHE:
           if self.valor_diaria < 2000:
               raise ValidationError({
                   "valor_diaria": "O valor da diária da Porsche deve ser no mínimo R$ 2000,00."
               })
                
            
        if self.marca == Marcas_Veiculo.FERRARI:
            if self.valor_diaria < 1500:
                raise ValidationError({
                    "valor_diaria": "O valor da diária da Ferrari deve ser no mínimo R$ 1500,00."
                })
        
        if self.marca == Marcas_Veiculo.FORD:
            if self.valor_diaria < 200:
                raise ValidationError({
                    "valor_diaria": "O valor da diária da Ford deve ser no mínimo R$ 200,00."
                })
            
        if self.marca == Marcas_Veiculo.LAMBORGHINI:
            if self.valor_diaria < 2000:
                raise ValidationError({
                    "valor_diaria": "O valor da diária da Lamborghini deve ser no mínimo R$ 2000,00."
                })
        
        if self.marca == Marcas_Veiculo.TESLA:
            if self.valor_diaria < 500:
                raise ValidationError({
                    "valor_diaria": "O valor da diária da Tesla deve ser no mínimo R$ 500,00."
                })
            
        if self.marca == Marcas_Veiculo.BUGATTI:
            if self.valor_diaria < 5000:
                raise ValidationError({
                    "valor_diaria": "O valor da diária da Bugatti deve ser no mínimo R$ 5000,00."
                })
        
    def save(self, *args, **kwargs):

        # Personalizar algo aqui

        self.marca = self.marca.title()
        self.modelo = self.modelo.title()
        self.placa = self.placa.upper()

        super().save(*args, **kwargs)
