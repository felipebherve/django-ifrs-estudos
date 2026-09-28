from rest_framework import serializers
from api.models import Conta
from django.core.exceptions import ValidationError


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'

    def validate(self, attrs):
        objeto = self.instance or self.Meta.model(**attrs)
        try:
            objeto.full_clean()
        except ValidationError as erro:
            raise serializers.ValidationError(erro.message_dict)

        return attrs