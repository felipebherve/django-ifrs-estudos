# Curso de Backend — IFRS + Instituto Hardware (Python e Django)

🇧🇷 Português · 🇺🇸 [English](README.md)

## Em que momento eu fiz isto

De **março a agosto de 2026** fiz o curso de backend oferecido pelo **IFRS** (Instituto Federal do Rio Grande do Sul) em parceria com o **Instituto Hardware**, online. Eu concluí o curso. Ele começa em "como pensar um problema" e termina construindo APIs REST em Django. Foi o curso que me deu as primeiras habilidades reais de backend.

Tudo aqui são minhas próprias anotações e códigos das aulas e exercícios.

## Como foi o curso

1. **Primeiro a lógica, depois o Python (mar–mai/2026, aulas 1 a 8).** Antes de qualquer sintaxe, o curso ensina a decompor um problema: o problema (sempre um verbo), os pressupostos, o contexto (os substantivos que uso) e as instruções numeradas. Guardei essas anotações em [`01_BACKEND (IFRS)/01_AULAS`](<01_BACKEND (IFRS)/01_AULAS>).
2. **Fundamentos de Python.** Variáveis, operadores, entrada e saída, strings, condicionais, laços e funções, com exercícios pequenos em [`02_EXERCICIOS`](<01_BACKEND (IFRS)/02_EXERCICIOS>) (soma, média, multiplicador, conversão de moeda, um teste de download, um exercício de redes e exercícios do Curso em Vídeo, como uma calculadora).
3. **Django (jun–ago/2026).** Estrutura de projeto, models e migrações, admin, relacionamentos (1:1, 1:N, N:N), validadores, enumerações e depois **APIs REST com Django REST Framework**. As anotações de aula datadas estão em [`04 DJANGO`](<01_BACKEND (IFRS)/04 DJANGO>), por exemplo: relacionamentos (01/07), APIs e CRUD (15/07), web services (30/07), um exercício de cálculo de frete (06/08) e a aula final (13/08).
4. **Desafio final:** o projeto TechTinga (veja abaixo).

## Os projetos

Todos estão em [`01_BACKEND (IFRS)/04 DJANGO/PROJETOS`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS>):

| Projeto | O que é | Stack |
|---------|---------|-------|
| [`techtinga-api`](https://github.com/felipebherve/techtinga-api) | **Desafio final.** API REST de gestão de projetos e tarefas, com importação de CSV e relatórios | Django, DRF |
| [`projeto_django`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/projeto_django>) | O projeto de aula: endpoints de saudação, cálculo e frete, e uma API de contas bancárias | Django, DRF |
| [`agencia_turismo`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/agencia_turismo>) | Uma agência de viagens para a Copa do Mundo (ingressos, passagens e pacotes) modelada com validação | Django |
| [`exercicios`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/exercicios>) | Models de exercício (alunos, disciplinas, voos) e um validador de CPF | Django |
| [`gremio`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/gremio>) | Meu primeiro projeto Django: um domínio de clube de futebol com validadores personalizados | Django |

## O que aprendi

Python (funções, arquivos, estruturas de dados), design orientado a objetos em Python, a arquitetura MVT do Django, modelagem relacional com o ORM, validação de dados, design de APIs REST (CRUD, serializers, rotas), leitura de arquivos CSV e sua importação, e leitura de documentação para resolver um problema que eu ainda não tinha visto.

## Situação

Concluído. Os próximos passos são praticar a escrita de testes automatizados para esses projetos e aprender fluxos de trabalho com Git em volta deles (é por isso que estou publicando).

## Rodando os projetos

Cada projeto tem seu próprio README com detalhes. Em geral:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```
