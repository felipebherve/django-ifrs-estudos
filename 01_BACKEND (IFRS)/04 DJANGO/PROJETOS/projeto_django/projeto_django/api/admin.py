from django.contrib import admin
from api.models import Aeroporto, AeroportoAdmin, Conta
# Register your models here.


admin.site.register(Aeroporto, AeroportoAdmin)
admin.site.register(Conta)