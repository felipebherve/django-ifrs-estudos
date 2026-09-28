from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class PalavrasProibidas:

    def __init__(self, black_list:list[str]= ['Inter'], message:str='Campo contém alguma palavra proibida, consulte as regras.'):
        if not isinstance(black_list, list):
            raise TypeError('Você deve informar uma lista de palavras proibidas')
        elif len(black_list) == 0:
            raise ValueError('A lista de palavras deve ter pelo menos uma palavra')
        for palavra in black_list:
            if not isinstance(palavra, str):
                raise TypeError('Todos os itens devem ser strings')
            
        if not isinstance(message, str):
            raise TypeError('Mensagem deve ser uma string')
        elif len(message) == 0:
            raise ValueError('Uma mensagem deve ser definida')
        
        self.black_list = black_list
        self.message = message

    def __call__(self, value):
        for palavra in self.black_list:
            if palavra.lower() in value.lower():
                raise ValidationError(self.message, params={'value':value})


        
    def __eq__(self, other):
        if isinstance(other, PalavrasProibidas):
            if len(other.black_list) == len(self.black_list):
                if other.black_list == self.black_list:
                    return True
        return False
