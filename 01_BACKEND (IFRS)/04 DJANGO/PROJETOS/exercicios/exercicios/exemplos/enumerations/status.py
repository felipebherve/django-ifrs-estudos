from django.db import models


class Status(models.TextChoices):
    DISPONIVEL = 'disponível', 'Disponível'
    EMITIDA = 'emitida', 'Emitida'
    EM_PROCESSAMENTO = 'em processamento', 'Em Processamento'
    CANCELADA = 'cancelada', 'Cancelada'
