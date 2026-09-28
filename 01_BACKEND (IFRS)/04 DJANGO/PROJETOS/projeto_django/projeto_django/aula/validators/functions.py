from django.core.exceptions import ValidationError


def validar_par(valor):
    try:
        if int(valor) % 2 != 0:
            raise ValidationError("Valor informado não é um número par.",
                                  params={"valor": valor})
    except:
        raise ValidationError("Valor informado não pode ser verificado!")
