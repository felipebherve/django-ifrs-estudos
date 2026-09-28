from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class ValidadorCPF:

    def __init__(self, message:str='CPF inválido'):
        if not isinstance(message, str):
            raise TypeError('Mensagem deve ser uma string')
        elif len(message) == 0:
            raise ValueError('Uma mensagem deve ser definida')
        
        self.message = message

    def __call__(self, value):
        cpf = ''.join(filter(str.isdigit, str(value)))
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValidationError(self.message, params={'value':value})
        
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                raise ValidationError(self.message, params={'value':value})

    def __eq__(self, other):
        return isinstance(other, ValidadorCPF) and self.message == other.message