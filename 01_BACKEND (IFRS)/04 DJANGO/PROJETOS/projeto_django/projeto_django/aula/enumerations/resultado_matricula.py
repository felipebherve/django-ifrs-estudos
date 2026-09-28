from django.db import models

class ResultadoMatricula(models.TextChoices):

    CANCELADA = "Cancelada", "Cancelada"
    MATRICULADO = "Matriculado", "Matriculado"
    EM_EXAME = "Em Exame", "Em Exame"
    APROVADO = "Aprovado", "Aprovado"
    APROVADO_EXAME = "Aprovado em Exame","Aprovado em Exame"
    REPROVADO_MEDIA = "Reprovado por Média", "Reprovado por Média"
    REPROVADO_MEDIA_FREQUENCIA = "Reprovado por Média/Frequência", "Reprovado por Média/Frequência"
    REPEOVADO_FREQUENCIA = "Reprovado por Frequência", "Reprovado por Frequência"