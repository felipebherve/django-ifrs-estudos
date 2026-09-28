from django.db import models
from django.utils.translation import gettext as _


class Status(models.TextChoices):
    PAGO = _('Pago'), 'Pago'
    EM_ABERTO = _('Em Aberto'), 'Em Aberto'
    CANCELADO = _('Cancelado'), 'Cancelado'

