from django.db import models

class Pagamento(models.TextChoices):
    CREDIT_CARD = 'CC', 'Cartão de Crédito'
    MONEY = 'MO', 'Dinheiro'
    PIX = 'PX', 'PIX'