# Django exercises — students, flights and a CPF validator

🇺🇸 English · 🇧🇷 [Português](README.pt-BR.md)

## Where I was when I made this

A practice project from **early July 2026**, during the Django classes of the IFRS + Instituto Hardware backend course, right after the lesson on relationships between models (01/07/2026). It's where I practiced modeling on my own.

## What's inside

The app is called `exemplos`:

| Model | Fields (summary) |
|-------|------------------|
| `Aluno` (student) | Name, **CPF** (validated), e-mail, phone, birth date, gender |
| `Disciplina` (course), `Matricula` (enrollment) | Students enrolled in courses, with a status |
| `Aeroporto`, `CompanhiaAerea`, `Voo`, `Passagem` | A small airline domain: airports, airlines, flights and tickets |

Along with them: enumerations (`disciplinas`, `genero`, `status`) and a custom validator.

### The CPF validator

[`exemplos/validators/validador_cpf.py`](exercicios/exemplos/validators/validador_cpf.py) is a reusable Django validator (`ValidadorCPF`) for the Brazilian CPF number. It removes punctuation, rejects sequences of the same digit, and checks the two verification digits with the official algorithm, returning a clear error message when the CPF is not valid.

## Run it

```bash
cd exercicios
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Use the admin at `http://127.0.0.1:8000/admin/` to create students and see the validator in action. It uses SQLite and development settings (`DEBUG = True`), for local study only.

## What I learned

Writing validators as classes (`@deconstructible`, `__call__`), the CPF verification-digit algorithm, one-model-per-file organization, enumerations and relationships between models.

## Next steps

Automated tests for the validator would be the natural next step: it has clear valid and invalid inputs, so it's a good first test target.

> The Django `SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable. If it isn't set, an insecure development key is used, so never deploy this project as it is.
