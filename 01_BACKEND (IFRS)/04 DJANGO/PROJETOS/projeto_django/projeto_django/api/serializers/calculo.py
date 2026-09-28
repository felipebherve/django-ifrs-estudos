from rest_framework import serializers
from api.enumerations import Operacoes


class CalculoSerializer(serializers.Serializer):
    valor1 = serializers.FloatField(required=True)
    valor2 = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required = True,choices = Operacoes.choices)
    resultado = serializers.FloatField(required=False)


    class Meta:
        fields = ['valor1', 'valor2', 'operacao']
    
    def calcular(self):
        nr1 = self.validated_data.get('valor1')
        nr2 = self.validated_data.get('valor2')
        op = self.validated_data.get('operacao')

        match op:
            case Operacoes.ADICAO:
                result = nr1+nr2
                self.validated_data.update({
                    'resultado':result, 
                    'operacao':Operacoes.ADICAO.label
                    })
            case Operacoes.SUBTRACAO:
                result = nr1-nr2
                self.validated_data.update({
                    'resultado':result, 
                    'operacao':Operacoes.SUBTRACAO.label
                    })
            case Operacoes.MULTIPLICACAO:
                result = nr1*nr2
                self.validated_data.update({
                    'resultado':result, 
                    'operacao':Operacoes.MULTIPLICACAO.label
                    })
            case Operacoes.DIVISAO:
                result = nr1/nr2
                self.validated_data.update({
                    'resultado':result, 
                    'operacao':Operacoes.DIVISAO.label
                    })
            case Operacoes.MODULO:
                result = nr1%nr2
                self.validated_data.update({
                    'resultado':result, 
                    'operacao':Operacoes.MODULO.label
                    })
            case _:
                raise NotImplementedError('Não Implementado')

