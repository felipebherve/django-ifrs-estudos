# Grêmio — meu primeiro projeto Django

🇧🇷 Português · 🇺🇸 [English](README.md)

## Em que momento eu fiz isto

Este é o **primeiro projeto Django** que criei na vida, no **início de julho de 2026**, nas primeiras aulas de Django do curso de backend do IFRS + Instituto Hardware. As anotações de aula ([`aula de django.txt`](../../aula%20de%20django.txt)) começam do zero: `pip install django`, `django-admin startproject "gremio"`, o `manage.py`, o que são `settings`, `urls`, `wsgi` e `asgi`, e como mudar o idioma e o fuso horário para o Brasil. Este projeto é onde digitei esses comandos pela primeira vez.

## O que tem aqui

O app se chama `clube` e tem três models de exemplo usados para praticar campos e validação:

| Model | O que pratica |
|-------|---------------|
| `Carro` | Vários tipos de campos e validadores: marca, modelo, ano, placa e chassi com tamanho fixo, cor, cor lateral, limites de velocidade e tipo de combustível |
| `Veiculo` | Um model de aluguel: valor da diária, seguro, indicadores de IPVA pago e de alugado |
| `Jogador` | Um jogador com título, descrição, qualidade (0–100) e uma nota (0–10) que não pode ser editada à mão |

### Validadores personalizados

Em [`clube/validators/`](gremio/gremio/clube/validators):

- `PalavrasProibidas`: uma classe validadora que recebe uma lista de palavras proibidas e uma mensagem, confere os próprios argumentos (tipos errados geram erros claros) e rejeita qualquer valor que contenha uma das palavras.
- `code.py` e `functions.py`: um validador de código e pequenas funções de validação (por exemplo, uma checagem de "números pares").

As enumerações (`cor`, `marca`, `marca2`, `tipo_combustivel`) são onde pratiquei a definição de opções para um campo.

## Como rodar

```bash
cd gremio/gremio
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois abra `http://127.0.0.1:8000/admin/`. Usa SQLite e configurações de desenvolvimento (`DEBUG = True`), só para estudo local.

## O que aprendi

A estrutura de um projeto Django, migrações (`makemigrations` e `migrate`), o admin, opções de campo (`blank`, `null`, `help_text`, `verbose_name`), validadores prontos e como escrever os meus, e opções com enumerações.

## Próximos passos

Este foi um laboratório de aprendizado. Os próximos projetos do curso ([`exercicios`](../exercicios), [`projeto_django`](../projeto_django) e [TechTinga](https://github.com/felipebherve/techtinga-api)) são os mais completos; aqui também faltam testes.

> A `SECRET_KEY` do Django é lida da variável de ambiente `DJANGO_SECRET_KEY`. Se ela não estiver definida, é usada uma chave de desenvolvimento insegura, então nunca publique este projeto em produção como está.
