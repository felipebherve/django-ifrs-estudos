from rest_framework import serializers
from api.enumerations import Regioes


class FreteSerializer(serializers.Serializer):
    peso = serializers.FloatField(required=True)
    regiao_origem = serializers.ChoiceField(required = True, choices = Regioes.choices)
    regiao_destino = serializers.ChoiceField(required = True, choices = Regioes.choices)
    valor_base = serializers.FloatField(required=False)
    adicional_peso = serializers.FloatField(required=False)
    adicional_regiao = serializers.FloatField(required=False)
    valor_total = serializers.FloatField(required=False)


    class Meta:
        fields = ['peso', 'regiao_origem', 'regiao_destino']
    
    def calcular(self):
        peso = self.validated_data.get('peso')
        self.validated_data.update({
            'valor_base':10.00
        })
        total = self.validated_data.get('valor_base')
        # ADICIONAL DE PESO-------------------------------------
        if peso < 0:
            raise ValueError('Peso deve ser maior que zero!!')

        if peso >= 0 and peso <= 1:
            self.validated_data.update({
                                'adicional_peso':0
                                })
            total= 0 + total

        if peso > 1 and peso <= 10:
            self.validated_data.update({
                'adicional_peso':5
            })
            total = 5 + total

        if peso > 10 and peso <= 20:
            self.validated_data.update({
                                'adicional_peso':20
                                })
            total= 20 + total

        if peso > 20:
            add_peso = float(35 + (((int(peso)-20)//10)*35))
            self.validated_data.update({
                                'adicional_peso':add_peso
                                })
            total= add_peso + total

        # ADICIONAL POR REGIÃO -----------------------------------
        r_o = self.validated_data.get('regiao_origem')
        r_d = self.validated_data.get('regiao_destino')

        if r_o == r_d:
            self.validated_data.update({
                                'adicional_regiao':10.00
                                })
            total = total+ 10.00

        elif (r_o == Regioes.SUL and r_d == Regioes.SUDESTE) or (r_o == Regioes.SUDESTE and r_d == Regioes.SUL):
            self.validated_data.update({
                                'adicional_regiao':15.00
                                })
            total = total+ 15.00

        elif r_o == Regioes.CENTRO_OESTE and (r_d == Regioes.SUL or r_d == Regioes.SUDESTE):
            self.validated_data.update({
                                'adicional_regiao':20.00
                                })
            total = total+ 20.00

        elif (r_o == Regioes.NORTE or r_o == Regioes.NORDESTE) and r_d == Regioes.CENTRO_OESTE:
            self.validated_data.update({
                                'adicional_regiao':30.00
                                })
            total = total+ 30.00

        else:
            self.validated_data.update({
                'adicional_regiao':50.00
            })
            total = total + 50.00

        self.validated_data.update({
            'valor_total':total
        })

        

        







        # else:
        #     raise NotImplementedError('Não Implementado')
