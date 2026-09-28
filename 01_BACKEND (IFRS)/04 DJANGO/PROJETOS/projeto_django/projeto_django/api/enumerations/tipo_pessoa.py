from django.db import models
from django.utils.translation import gettext as _

class TipoPessoa(models.TextChoices):
    PF = 'PF', _('Pessoa Física')
    PJ = 'PJ', _('Pessoa Jurídica')