import contextlib, io
from manage import *

# define que a saída será o terminal
saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()


# a partir daqui podemos utilizar como no terminal

from aula.models import Pessoa
from datetime import date

sergio = Pessoa(
    nome = 'Sergio Anubis',
    cpf = '01234567890',
    data_nascimento = date(1990, 12, 31)
)

sergio.full_clean()
sergio.save()

acosta = Pessoa(
    nome = 'Acosta Silva',
    cpf = "00000000000",
    data_nascimento = date(1980,5,15)
)


print(f'Objeto criado : {sergio}')
print(f'Objeto criado : {acosta}')

acosta.full_clean()
acosta.save()
