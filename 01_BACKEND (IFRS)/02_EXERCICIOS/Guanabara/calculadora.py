n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número: '))
operador = input('Operação: ')

def operacao(operador):
    if operacao == "+":
      return f'A operação {n1}{operador}{n2} = {n1+n2}'
    elif operacao == "/":
        return f'A operação {n1}{operador}{n2} = {n1/n2}'
    elif operacao == "*":
        return f'A operação {n1}{operador}{n2} = {n1*n2}'
    elif operacao == "-":
        return f'A operação {n1}{operador}{n2} = {n1-n2}'
    else:
        return f'A operação "{operador}" é inválida.'
print(operacao(operacao))
