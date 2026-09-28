from email.policy import default
from django.db import models
from aula.models import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from aula.enumerations import Marca, TipoCombustivel, Cor, CorLateral


class Carro(BaseModel):
    # Atributos de classe
    marca = models.CharField(validators=[MinLengthValidator(2)],
                             max_length=25,
                             choices=Marca,
                             default=Marca.BYD,
                             verbose_name="Marca",
                             help_text="A Marca deve conter no mínimo 2 caracteres e no máximo 25.")

    modelo = models.CharField(validators=[MinLengthValidator(2)],
                              max_length=25,
                              verbose_name="Modelo",
                              help_text="O Modelo deve conter no mínimo 2 caracteres e no máximo 25.")

    ano = models.IntegerField(validators=[MaxValueValidator(2026)],
                              verbose_name="Ano",
                              help_text="O Ano deve ser no máximo o ano atual.")

    placa = models.CharField(max_length=8,
                             verbose_name="Placa",
                             help_text="A Placa deve conter no máximo 8 caracteres.")

    chassi = models.CharField(max_length=13,
                              verbose_name="Chassi",
                              help_text="O Chassi deve ter no máximo 13 caracteres.")

    cor = models.IntegerField(choices=Cor,
                              default=Cor.AZUL,
                              verbose_name="Cor",
                              help_text="A Cor deve conter no mínimo 4 caracteres e no máximo 20.")

    cor_lateral = models.IntegerField(verbose_name="Cor Lateral",
                                      choices=Cor,
                                      default=Cor.AZUL,
                                      help_text="A Cor Lateral deve conter no mínimo 4 caracteres e no máximo 20.")

    velocidade = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(500.0)],
                                   verbose_name="Velocidade",
                                   help_text="A Velocidade deve ser valor entre 0.0 e 500.")

    tipo_combustivel = models.CharField(validators=[MinLengthValidator(2)],
                             max_length=15,
                             choices=TipoCombustivel,
                             default=TipoCombustivel.GASOLINA,
                             verbose_name="Tipo Combustivel",
                             help_text="O Tipo de Combustivel deve ter no mínimo 2 caracteres e no máximo 15.")

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.ano} - {self.placa} - {self.chassi} - {self.get_cor_display()} - {self.get_cor_lateral_display()} - {self.velocidade} - {self.tipo_combustivel}"
