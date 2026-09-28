# Projeto de aula — exercícios de Django + API REST

🇧🇷 Português · 🇺🇸 [English](README.md)

## Em que momento eu fiz isto

Este é o projeto que construí **durante as aulas de Django** do curso de backend do IFRS + Instituto Hardware (julho–agosto de 2026). Fui acrescentando coisas a ele aula após aula: primeiro models e relacionamentos, depois os primeiros endpoints de API, depois um exercício de verdade. É onde eu praticava cada ideia nova assim que era explicada.

Moram aqui dois apps:

- **`aula`** — models das aulas de modelagem (alunos, cursos, matrículas, bolsas, carros, aeroportos e companhias aéreas), com enumerações e validadores.
- **`api`** — o lado da API REST, feito com Django REST Framework.

## O que tem na API

| Rota (em `api/urls.py`) | O que faz |
|-------------------------|-----------|
| `funcao/saudacao/<nome>/` e `classe/saudacao/<nome>/` | O mesmo endpoint de saudação escrito como **view de função** e como **view de classe**, para comparar os dois estilos |
| `funcao/numeros/<n>/` e `classe/numeros/<n>/` | Mesma ideia com um número como parâmetro |
| `funcao/calculo/` e `classe/calculo/` | Endpoint de cálculo (versões função e classe) |
| `classe/login_teste/`, `classe/numero_teste/` | Endpoints pequenos para praticar o recebimento e a validação de dados |
| `calcular/frete/` | **Calculadora de frete** (exercício de aula de 06/08/2026, veja abaixo) |
| `aeroporto/<id>/` | Ler um objeto aeroporto |
| `conta/` | Um **CRUD de contas bancárias** (a pagar / a receber) usando um router do DRF |

### O exercício de cálculo de frete

Faça um `POST` com um JSON como `{"peso": 10.5, "regiao_origem": "SUL", "regiao_destino": "NORDESTE"}` e a API responde com o valor base (que depende do par de regiões de origem e destino), o adicional de peso (que cresce por faixa de peso), o adicional de região e o total. As regras vieram do exercício da aula e estão nas minhas anotações em [`../../compilado.txt`](../../compilado.txt).

### A API de contas bancárias

`Conta` tem favorecido, documento (CPF/CNPJ), data de vencimento, data de pagamento, valor, tipo de pessoa, tipo de conta (a pagar ou a receber) e status. O domínio é próximo do meu trabalho anterior em finanças (contas a pagar e a receber).

## Como rodar

```bash
cd projeto_django
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

Usa SQLite e configurações de desenvolvimento (`DEBUG = True`), só para estudo local.

## O que aprendi

A diferença entre views de função e de classe, serializers e routers do DRF, requisição e resposta em JSON, validadores e enumerações, e como organizar um app em pastas (`models/`, `views/`, `serializers/`) em vez de um arquivo gigante.

## Próximos passos

Testes automatizados para os endpoints (os arquivos de teste ainda são o modelo padrão) e autenticação.

> A `SECRET_KEY` do Django é lida da variável de ambiente `DJANGO_SECRET_KEY`. Se ela não estiver definida, é usada uma chave de desenvolvimento insegura, então nunca publique este projeto em produção como está.
