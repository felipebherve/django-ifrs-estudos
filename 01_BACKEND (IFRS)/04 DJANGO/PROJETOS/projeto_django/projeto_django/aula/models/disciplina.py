from aula.models import BaseModel, Curso, AlunoCurso
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class Disciplina(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)],
        help_text="Insira o nome da disciplina."
    )
    ementa = models.TextField(
        null=True, blank=True,
        max_length=5000,
        help_text="Insira a ementa da disciplina até 5000 caracteres."
    )

    curso = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(3)],
        help_text="Selecione o curso da disciplina.",
        choices=Curso,
    )

    carga_horaria = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(20),
                    MaxValueValidator(160)],
        help_text="Informe a carga horária da disciplina.",
        verbose_name="Carga Horária"
    )

    alunos = models.ManyToManyField(
        AlunoCurso,
        null= True, blank=True,
        through="Matricula",
        through_fields=("disciplina", "aluno")
    )

    def __str__(self) -> str:
        return f"{self.nome}/{self.carga_horaria} ({self.curso})"
