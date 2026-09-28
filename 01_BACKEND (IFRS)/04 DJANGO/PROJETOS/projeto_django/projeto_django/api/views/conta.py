from rest_framework import viewsets
from api.serializers.conta import ContaSerializer
from api.models import Conta


class ContaService(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()