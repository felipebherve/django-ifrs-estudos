# instanciacao das variaveis -- contexto

Nota1 = 0.0
Nota2 = 0.0
Nota3 = 0.0
Nota4 = 0.0
Nota5 = 0.0
MediaA = 0.0
somanotas = 0.0


# Entrada de dados
print('Este programa imprime a media do aluno')
Nota1 = float(input('Digite a Primeira nota '))
Nota2 = float(input('Digite a Segunda nota '))
Nota3 = float(input('Digite a Terceira nota '))
Nota4 = float(input('Digite a Quarta nota '))
Nota5 = float(input('Digite a Quinta nota '))

# Processamento
somanotas = float(Nota1+Nota2+Nota3+Nota4+Nota5)
MediaA = float(somanotas/5)


#saida de dados 
print('A media do aluno é: ', MediaA)
