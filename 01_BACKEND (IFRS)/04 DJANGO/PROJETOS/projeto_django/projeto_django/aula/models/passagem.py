from django.core.validators import MinLengthValidator
from django.db import models
from aula.models import BaseModel,Voo
from aula.enumerations import Status


class Passagem(BaseModel):

    nr = models.PositiveSmallIntegerField(
         verbose_name="Número da Passagem",
         help_text="Informe o número da passagem no Vôo.",
    )

    passageiro = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
        help_text="Informe o nome do passageiro."
    )

    status = models.CharField(
        max_length=20,
        help_text="Selecione o atual Status da passagem.",
        choices=Status
    )

    poltrona = models.CharField(
        max_length=3,
        validators= [MinLengthValidator(3)],
        help_text="Informe a localização da poltrona."
    )

    voo = models.ForeignKey(
        Voo,
        on_delete=models.RESTRICT,
        # CASCADE: (deleta em forma de cascata),
        # PROTECT: (não deixa deletar),
        # RESTRICT: (Avisa que não pode),
        # SET_NULL: (seta nulo, mas tem que ter blank=True, Null=true),
        # SET_DEFAULT: (Coloca o default mas deve ter o default definido.)
        verbose_name="Vôo Comercial",
        help_text="Selecione o vôo comercial"
    )

    def __str__(self):
        return f"{self.voo} - {self.nr} - {self.poltrona}: {self.passageiro}"

    class Meta:
        verbose_name_plural = "Passagens"
        unique_together = [['nr', 'voo'], ['passageiro', 'voo']]