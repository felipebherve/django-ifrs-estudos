# Exercícios de Django — alunos, voos e um validador de CPF

🇧🇷 Português · 🇺🇸 [English](README.md)

## Em que momento eu fiz isto

Um projeto de prática do **início de julho de 2026**, durante as aulas de Django do curso de backend do IFRS + Instituto Hardware, logo depois da aula sobre relacionamentos entre models (01/07/2026). É onde eu praticava modelagem por conta própria.

## O que tem aqui

O app se chama `exemplos`:

| Model | Campos (resumo) |
|-------|-----------------|
| `Aluno` | Nome, **CPF** (validado), e-mail, telefone, data de nascimento, gênero |
| `Disciplina`, `Matricula` | Alunos matriculados em disciplinas, com um status |
| `Aeroporto`, `CompanhiaAerea`, `Voo`, `Passagem` | Um pequeno domínio de aviação: aeroportos, companhias, voos e passagens |

Junto com eles: enumerações (`disciplinas`, `genero`, `status`) e um validador personalizado.

### O validador de CPF

[`exemplos/validators/validador_cpf.py`](exercicios/exemplos/validators/validador_cpf.py) é um validador reutilizável do Django (`ValidadorCPF`) para o CPF brasileiro. Ele remove a pontuação, rejeita sequências do mesmo dígito e confere os dois dígitos verificadores com o algoritmo oficial, devolvendo uma mensagem de erro clara quando o CPF não é válido.

## Como rodar

```bash
cd exercicios
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Use o admin em `http://127.0.0.1:8000/admin/` para criar alunos e ver o validador em ação. Usa SQLite e configurações de desenvolvimento (`DEBUG = True`), só para estudo local.

## O que aprendi

Escrever validadores como classes (`@deconstructible`, `__call__`), o algoritmo do dígito verificador do CPF, a organização de um model por arquivo, enumerações e relacionamentos entre models.

## Próximos passos

Testes automatizados para o validador seriam o passo natural: ele tem entradas válidas e inválidas bem claras, então é um bom primeiro alvo de teste.

> A `SECRET_KEY` do Django é lida da variável de ambiente `DJANGO_SECRET_KEY`. Se ela não estiver definida, é usada uma chave de desenvolvimento insegura, então nunca publique este projeto em produção como está.
