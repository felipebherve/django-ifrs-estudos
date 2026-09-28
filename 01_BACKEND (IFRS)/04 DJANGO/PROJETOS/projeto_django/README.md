# Class project — Django + REST API exercises

🇺🇸 English · 🇧🇷 [Português](README.pt-BR.md)

## Where I was when I made this

This is the project I built **during the Django classes** of the IFRS + Instituto Hardware backend course (July–August 2026). I kept adding to it lesson after lesson: first models and relationships, then the first API endpoints, then a real exercise. It's where I practiced each new idea as soon as it was explained.

Two apps live here:

- **`aula`** — models from the modeling classes (students, courses, enrollments, scholarships, cars, airports and airlines), with enumerations and validators.
- **`api`** — the REST API side, built with Django REST Framework.

## What's in the API

| Route (in `api/urls.py`) | What it does |
|--------------------------|--------------|
| `funcao/saudacao/<name>/` and `classe/saudacao/<name>/` | The same greeting endpoint written as a **function view** and as a **class-based view**, to compare both styles |
| `funcao/numeros/<n>/` and `classe/numeros/<n>/` | Same idea with a number parameter |
| `funcao/calculo/` and `classe/calculo/` | Calculation endpoint (function and class versions) |
| `classe/login_teste/`, `classe/numero_teste/` | Small endpoints to practice receiving and validating data |
| `calcular/frete/` | **Shipping cost calculator** (class exercise of 06/08/2026, see below) |
| `aeroporto/<id>/` | Read an airport object |
| `conta/` | A **CRUD for bank accounts** (payable / receivable) using a DRF router |

### The shipping-cost exercise

`POST` a JSON like `{"peso": 10.5, "regiao_origem": "SUL", "regiao_destino": "NORDESTE"}` and the API answers with the base value (which depends on the origin/destination region pair), the weight surcharge (which grows by weight band), the region surcharge and the total. The rules came from the class exercise and are kept in my notes in [`../../compilado.txt`](../../compilado.txt).

### The bank-account API

`Conta` has beneficiary, document (CPF/CNPJ), due date, payment date, amount, person type, account type (payable or receivable) and status. The domain is close to my earlier work in finance (accounts payable and receivable).

## Run it

```bash
cd projeto_django
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

It uses SQLite and development settings (`DEBUG = True`), for local study only.

## What I learned

The difference between function-based and class-based views, DRF serializers and routers, request/response as JSON, validators and enumerations, and how to organize an app in folders (`models/`, `views/`, `serializers/`) instead of one giant file.

## Next steps

Automated tests for the endpoints (the test files are still the default template) and authentication.

> The Django `SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable. If it isn't set, an insecure development key is used, so never deploy this project as it is.
