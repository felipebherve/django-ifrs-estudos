from aula.models import BaseModel, AlunoCurso, Disciplina
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
from aula.enumerations import ResultadoMatricula
from datetime import date
from django.contrib import admin


class Matricula(BaseModel):

    ano = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2000),
                    MaxValueValidator(2100)],
        help_text="Informe o ano da matrícula."
    )

    semestre = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(2)],
        help_text="Informe o semestre da matrícula."
    )

    frequencia = models.FloatField(
        validators=[MinValueValidator(0.0),
                    MaxValueValidator(100.0)],
        verbose_name="Frequência do estudante.",
        help_text="Informe a frequência do estudante"
    )

    nota = models.FloatField(
        validators=[MinValueValidator(0.0),
                    MaxValueValidator(10.0)],
        help_text="Informe a nota do aluno."
    )

    status = models.CharField(
        max_length=35,
        validators=[MinLengthValidator(3)],
        help_text="Informe a nota final do aluno.",
        choices=ResultadoMatricula,
    )

    matriculado_em = models.DateTimeField(
        # (Quando foi criado): Seta o valor em que este registro foi Criado.
        # auto_created=True
        auto_now_add=True,
        help_text="Informe a data/hora da matrícula."
    )

    alterado_em = models.DateTimeField(
        # (Quando foi alterado): Seta o valor em que este registro foi Alterado.
        auto_now=True,
        help_text="Informe a data/hora da alteração."
    )

    aluno = models.ForeignKey(
        AlunoCurso,
        on_delete=models.RESTRICT,
        help_text="Selecione o aluno para matrícula."
    )

    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.RESTRICT,
        help_text="Selecione a disciplina para a matrícula."
    )

    class Meta:
        # Ele não deixa repetir o mesmo Aluno na mesma Disciplina no mesmo Ano no mesmo Semestre, os quatro atributos precisam ser iguais para ele não permitir.
        unique_together = [["aluno", "disciplina", "ano", "semestre"]]

    def clean(self):

        hoje = date.today()
        if self.ano != hoje.year:
            raise ValidationError({
                "ano": "Ano inválido para matrícula"
            })

# Para o django "substituto" do datetime
# from django.utils import timezone
# from datetime import datetime

    def __str__(self) -> str:
        return f"{self.ano}/{self.semestre} {self.aluno.nome} - {self.disciplina.nome}: {self.status} - {self.matriculado_em.astimezone().strftime('%d/%m/%y - %H:%M')}"
                          # Mostra no formato brasileiro a data e a hora, além de considerar o timezone da America/Sao Paulo que foi definido no settings.py.

class MatriculaAdmin(admin.ModelAdmin):
    # Os campos que devem ser exibidos no admin
    list_display = ("ano", "semestre", "aluno", "disciplina", "status", "__str__")

    # Quais campos não devem ser permitidos alteração
    readonly_fields = ("alterado_em", "matriculado_em")

    # Os campos que dejamos fazer buscas.
    # (Por ser uma Tupla ponha uma vírgula no fim para não dar erro.)
    search_fields = ("ano",)

    # Os campos que desejamos a opção de filtro
    list_filter = ("ano", "disciplina", "status")