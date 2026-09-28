from django.contrib import admin
from aula.models import Exemplo
from aula.models import Carro
from aula.models import Veiculo, Pessoa,Passaporte, Aluno, Bolsa, Voo, Passagem, Aeroporto, AeroportoAdmin, CompanhiaAerea, AlunoCurso, Disciplina, Matricula, MatriculaAdmin

# Register your models here.
admin.site.register(Exemplo)
admin.site.register(Carro)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Passaporte)
admin.site.register(Aluno)
admin.site.register(Bolsa)
admin.site.register(Voo)
admin.site.register(Passagem)
admin.site.register(Aeroporto, AeroportoAdmin)
admin.site.register(CompanhiaAerea)
admin.site.register(AlunoCurso)
admin.site.register(Disciplina)
admin.site.register(Matricula, MatriculaAdmin)