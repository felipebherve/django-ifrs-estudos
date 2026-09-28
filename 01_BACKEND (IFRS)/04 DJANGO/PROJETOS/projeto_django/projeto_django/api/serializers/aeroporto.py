from rest_framework import serializers
from api.enumerations import Operacoes
from ..models import Aeroporto


class AeroportoSerializer(serializers.ModelSerializer):
    

    class Meta: #subclasse para configuração da superclasse
        model = Aeroporto
        fields = '__all__'
