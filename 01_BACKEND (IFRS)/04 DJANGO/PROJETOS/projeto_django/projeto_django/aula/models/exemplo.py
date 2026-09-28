from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from aula.models import BaseModel
from django.db import models
from aula.validators import validar_par, CodeValidator, PalavrasProibidas
from django.core.exceptions import ValidationError

class Exemplo(BaseModel):
    # Atributos de classe
    titulo = models.CharField(max_length=100,
                              validators=[MinLengthValidator(5), PalavrasProibidas(["Inter", "Admin", "Root", "Colorado"])],
                              verbose_name="Título do Exemplo",
                              help_text="O título deve conter pelo menos 5 caracteres e no máximo 100 caracteres.")

    descricao = models.TextField(max_length=5000,
                                 blank=True, null=True,
                                 validators=[MinLengthValidator(10),
                                             PalavrasProibidas(["Inter", "Admin", "Root", "Colorado"])],
                                 verbose_name="Descrição",
                                 help_text="Informe a descrição do exemplo, esta descrição ficará disponível para o usuário.")

    qualidade = models.IntegerField(default=0,
                                    validators=[MinValueValidator(0), MaxValueValidator(100)],
                                    verbose_name="Qualidade",
                                    help_text="A qualidade do exemplo deve estar entre 0 e 100.")

    nota = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                             verbose_name="Nota",
                             help_text="A nota do exemplo deve estar entre 0.0 e 10.0.")

    numeros_pares = models.IntegerField(default=0, unique=True,
                                        verbose_name="Número",
                                        validators=[validar_par, CodeValidator(200)],
                                        help_text="Insira o seu número escolhido. Lembre-se que apenas são aceitos números pares e únicos.")

    codigo = models.IntegerField(blank=True, null=True,
                                 verbose_name="Código",
                                 help_text="Insira o código",
                                 validators=[CodeValidator(100)])

    class Meta:
        verbose_name = "Exemplo"
        verbose_name_plural = "Exemplos"

    def __str__(self):
        return f"{self.titulo} - {self.descricao} - {self.qualidade} - {self.nota} - {self.numeros_pares} - {self.codigo}"

    # Validador crossfield
    def clean(self):
        # self.nota    self.qualidade
        if self.nota != None and self.qualidade != None:

            if self.nota * 10 < self.qualidade - 10:
                raise ValidationError({
                    "nota": "Nota e qualidade não são equivalentes.",
                    "qualidade": "Qualidade e nota não são equivalentes."
                })

            if (self.qualidade + 10) / 10 < self.nota:
                raise ValidationError({
                    "qualidade": "Qualidade e nota não são equivalentes.",
                    "nota": "Nota e qualidade não são equivalentes."
                })

        if self.titulo in self.descricao:
            raise ValidationError({
                "descricao": "A descrição não pode conter o título."
            })



    def save(self, *args, **kwargs):

        # Personalizar algo aqui
        self.titulo = self.titulo.title()
        if self.descricao == "" or self.descricao == None:
            self.descricao = "Descrição não informada"
        self.descricao = self.descricao.capitalize()

        super().save(*args, **kwargs)
