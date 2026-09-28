from django.core.validators import MinLengthValidator
from django.db import models
from aula.models import BaseModel
from django.contrib import admin

class Aeroporto(BaseModel):

    cod = models.CharField(
        verbose_name="Código do Aeroporto",
        help_text="Informe o código da companhia.",
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    cidade = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        help_text="Informe a cidade do aeroporto."
    )

    pais = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        verbose_name="país",
        help_text="Informe o país do aeroporto.",
    )

    def __str__(self):
        return f"{self.cod}"

#  Configurações do admin
class AeroportoAdmin(admin.ModelAdmin):
    list_display = ("cod", "cidade", "pais")
    search_fields = ("pais", "cod")
    list_filter = ("cidade",)
