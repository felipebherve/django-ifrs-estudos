from django.db import models

class Setor(models.TextChoices):
    STAND = 'ST', 'Arquibancada (Stand)'
    SEAT = 'SE', 'Assento (Seat)'
    CABIN = 'CA', 'Cabine (Cabin)'
    COMMON = 'CO', 'Área Comum (Common Area)'