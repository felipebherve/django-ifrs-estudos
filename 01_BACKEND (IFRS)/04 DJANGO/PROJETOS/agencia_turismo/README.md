# World Cup Travel Agency — Django models & validation

🇺🇸 English · 🇧🇷 [Português](README.pt-BR.md)

## Where I was when I made this

I built this in **July 2026**, in the first weeks of the Django part of the IFRS + Instituto Hardware backend course. The project is based on a **UML class diagram** for a travel agency that sells trips to a football World Cup, and the goal was to turn it into working Django models: fields, validation rules, choices and relationships. The diagram is in [`docs/agencia_turismo.png`](docs/agencia_turismo.png).

## What it models

The app is called `fifacwc` and has three models plus four sets of choices:

| Model | What it represents |
|-------|-------------------|
| `Ingresso` (ticket) | Ticket holder, passport, purchase date, price, stadium, section, game date, tournament phase and city |
| `Passagem` (flight ticket) | Flight code, origin, destination, departure and arrival, holder, passport, price and airline |
| `Pacote` (package) | The person responsible, e-mail, purchase date, total price and payment method, linking the tickets and flights that were sold together |

| Choices (`enumerations/`) | Values |
|---------------------------|--------|
| `Fase` | Group stage, round of 16, quarter-finals, semi-final, final |
| `Setor` | Stand, seat, cabin, common area |
| `Pagamento` | Credit card, cash, PIX |
| `Companhia` | Airlines |

Validation lives in the fields (minimum lengths, minimum values such as a price that can't be negative, dates that can't be in the past) and in the shared `BaseModel`.

## Run it

You can explore everything through the Django admin:

```bash
cd agencia_turismo
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open `http://127.0.0.1:8000/admin/`. It uses SQLite and development settings (`DEBUG = True`), for local study only.

## What I learned

Turning a UML diagram into models, foreign keys and relationship cardinality (`0..1`, `0..*`), field validators, `TextChoices` enumerations, splitting models into one file each, and reading Django's error messages when a migration doesn't match the models.

## Next steps

There is no API or custom screens yet; this project is only the data layer. Automated tests are also missing (the `tests.py` file is the default template).

> The Django `SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable. If it isn't set, an insecure development key is used, so never deploy this project as it is.
