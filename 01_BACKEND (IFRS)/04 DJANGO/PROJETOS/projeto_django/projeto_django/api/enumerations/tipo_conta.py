from django.db import models
from django.utils.translation import gettext as _

class TipoConta(models.TextChoices):
    PAGAR = _('PAGAR'), 'A Pagar'
    RECEBER = _('RECEBER'), 'A Receber'