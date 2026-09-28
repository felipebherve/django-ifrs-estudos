# Grêmio — my first Django project

🇺🇸 English · 🇧🇷 [Português](README.pt-BR.md)

## Where I was when I made this

This is the **first Django project** I ever created, in **early July 2026**, in the first Django classes of the IFRS + Instituto Hardware backend course. The class notes ([`aula de django.txt`](../../aula%20de%20django.txt)) start at the very beginning: `pip install django`, `django-admin startproject "gremio"`, `manage.py`, what `settings`, `urls`, `wsgi` and `asgi` are, and how to change the language and time zone to Brazil. This project is where I typed those commands for the first time.

## What's inside

The app is called `clube` and has three example models used to practice fields and validation:

| Model | What it practices |
|-------|-------------------|
| `Carro` | Many kinds of fields and validators: brand, model, year, plate and chassis with fixed lengths, colour, side colour, speed limits and fuel type |
| `Veiculo` | A rental-style model: daily rate, insurance, tax paid and rented flags |
| `Jogador` | A player with a title, description, quality (0–100) and a grade (0–10) that can't be edited by hand |

### Custom validators

In [`clube/validators/`](gremio/gremio/clube/validators):

- `PalavrasProibidas`: a validator class that receives a list of forbidden words and a message, checks its own arguments (wrong types raise clear errors) and rejects any value that contains one of the words.
- `code.py` and `functions.py`: a code validator and small validation functions (for example, an "even numbers" check).

The enumerations (`cor`, `marca`, `marca2`, `tipo_combustivel`) are where I practiced defining choices for a field.

## Run it

```bash
cd gremio/gremio
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open `http://127.0.0.1:8000/admin/`. It uses SQLite and development settings (`DEBUG = True`), for local study only.

## What I learned

The Django project layout, migrations (`makemigrations` and `migrate`), the admin, field options (`blank`, `null`, `help_text`, `verbose_name`), built-in validators and how to write my own, and choices with enumerations.

## Next steps

This was a learning sandbox. The next projects in the course ([`exercicios`](../exercicios), [`projeto_django`](../projeto_django) and [TechTinga](https://github.com/felipebherve/techtinga-api)) are the more complete ones; tests are still missing here too.

> The Django `SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable. If it isn't set, an insecure development key is used, so never deploy this project as it is.
