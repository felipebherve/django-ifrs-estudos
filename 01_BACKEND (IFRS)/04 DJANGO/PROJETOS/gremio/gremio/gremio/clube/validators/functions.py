from django.core.exceptions import ValidationError
from datetime import date

def validation_even(valor):
    try:
        if (int(valor) % 2) !=0:
            raise ValidationError('O valor informado não é par',
                                   params={'Valor': valor }) 
    except ValueError:
        raise ValidationError('Valor informado não pode ser verificado!')
    except TypeError:
        raise ValidationError('Valor informado não pode ser verificado!')
    
def validation_ano_do_modelo(ano):
    if ano < (date.today().year -5):
        raise ValidationError('O ano deve ser no máximo menor que 5 anos do atual')
    if ano > (date.today().year +1):
        raise ValidationError('O ano deve ser menor que o ano atual +1')  