# instanciacao das variaveis -- contexto
real = 0
taxa_dolar = 0
resultado = 0

# ENTRADA DE DADOS
print('Esse programa converte o real em dólar.')
real = float(input('Qual valor em real deseja converter para dólar? '))
taxa_dolar = float(input('Qual a taxa atual do dólar? '))

# PROCESSAMENTO DE DADOS
resultado = float(real/taxa_dolar)
print('O valor de ', real,' em dolares é: ', resultado)