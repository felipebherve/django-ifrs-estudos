from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


#decorator que permite "descontruir" / "serializar" um novo
#validador, ou seja, construir e reconstruir um validador
@deconstructible
class CodeValidator:
    #metodo para criar/instanciar o validador
    def __init__(self, code:int=0):
        if not isinstance(code,int):
            raise TypeError('Code deve obrigatoriamente ser um int')
        self.code = code
        
        #metodo que realiza a validação
    def __call__(self, value):
        try:
            value = int(value)
            if value == self.code:
                raise ValidationError('Valor não permitido!', params={'value':value})
        except ValueError as e:
            raise ValueError(e)
        except TypeError as e:
            raise TypeError(e)
        
        #metodo que verifica se o validador já existe
        #e permite a serialização (construção/reconstrução)
        #metodo equals
    def __eq__(self, other):
        return (isinstance(other, CodeValidator)
                and self.code == other.code)