# Backend course — IFRS + Instituto Hardware (Python & Django)

🇺🇸 English · 🇧🇷 [Português](README.pt-BR.md)

## Where I was when I made this

From **March to August 2026** I took the backend course offered by the **IFRS** (Instituto Federal do Rio Grande do Sul) together with **Instituto Hardware**, online. I completed it. It starts from "how to think about a problem" and ends with building REST APIs in Django. This is the course that gave me my first real backend skills.

Everything here is my own notes and code from the classes and exercises.

## How the course went

1. **Logic first, then Python (Mar–May 2026, classes 1–8).** Before any syntax, the course teaches how to break a problem down: the problem (always a verb), the assumptions, the context (the nouns you use) and the numbered instructions. I kept these notes in [`01_BACKEND (IFRS)/01_AULAS`](<01_BACKEND (IFRS)/01_AULAS>).
2. **Python fundamentals.** Variables, operators, input/print, strings, conditionals, loops and functions, with small exercises in [`02_EXERCICIOS`](<01_BACKEND (IFRS)/02_EXERCICIOS>) (sum, average, multiplier, currency conversion, a download test, a networks exercise, and Curso em Vídeo exercises such as a calculator).
3. **Django (Jun–Aug 2026).** Project structure, models and migrations, admin, relationships (1:1, 1:N, N:N), validators, enumerations, then **REST APIs with Django REST Framework**. The dated lesson notes are in [`04 DJANGO`](<01_BACKEND (IFRS)/04 DJANGO>), for example: relationships (01/07), APIs and CRUD (15/07), web services (30/07), a shipping-cost exercise (06/08) and the final class (13/08).
4. **Final challenge:** the TechTinga project (see below).

## The projects

All of them are in [`01_BACKEND (IFRS)/04 DJANGO/PROJETOS`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS>):

| Project | What it is | Stack |
|---------|-----------|-------|
| [`techtinga-api`](https://github.com/felipebherve/techtinga-api) | **Final challenge.** Project and task management REST API with CSV import and reports | Django, DRF |
| [`projeto_django`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/projeto_django>) | The class project: greetings, calculation and shipping-cost endpoints, plus a bank-account API | Django, DRF |
| [`agencia_turismo`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/agencia_turismo>) | A World Cup travel agency (tickets, flights and packages) modeled with validation | Django |
| [`exercicios`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/exercicios>) | Exercise models (students, courses, flights) and a CPF validator | Django |
| [`gremio`](<01_BACKEND (IFRS)/04 DJANGO/PROJETOS/gremio>) | My first Django project: a football club domain with custom validators | Django |

## What I learned

Python (functions, files, data structures), object-oriented design in Python, the Django MVT architecture, relational modeling with the ORM, data validation, REST API design (CRUD, serializers, routes), reading CSV files and importing them, and reading documentation to solve a problem I hadn't seen before.

## Status

Completed. The next steps are to practice writing automated tests for these projects and to learn Git-based workflows around them (that's why I'm publishing them).

## Running the projects

Each project has its own README with details. In general:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```
