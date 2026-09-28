from django.db import models

class Fase(models.TextChoices):
    GRUPO = 'GR', 'Grupo'
    ROUND_16 = 'OIT', 'Oitavas de Final'
    QUARTER = 'QUA', 'Quartas de Final'
    SEMIFINAL = 'SEM', 'Semifinal'
    FINAL = 'FIN', 'Final'   