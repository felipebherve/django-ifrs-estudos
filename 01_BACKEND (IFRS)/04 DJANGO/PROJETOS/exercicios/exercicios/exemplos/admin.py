from django.contrib import admin
from exemplos.models import Voo, Passagem, Aeroporto, AeroportoAdmin, CompanhiaAerea, Aluno, Disciplina, Matricula 

# Register your models here.

admin.site.register(Voo)
admin.site.register(Passagem)
admin.site.register(Aeroporto, AeroportoAdmin)
admin.site.register(CompanhiaAerea)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Matricula)

