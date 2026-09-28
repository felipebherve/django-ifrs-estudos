# Agência de Turismo da Copa do Mundo — models e validação em Django

🇧🇷 Português · 🇺🇸 [English](README.md)

## Em que momento eu fiz isto

Fiz este projeto em **julho de 2026**, nas primeiras semanas da parte de Django do curso de backend do IFRS + Instituto Hardware. O projeto parte de um **diagrama de classes UML** de uma agência de viagens que vende pacotes para uma Copa do Mundo de futebol, e o objetivo era transformá-lo em models do Django funcionando: campos, regras de validação, opções e relacionamentos. O diagrama está em [`docs/agencia_turismo.png`](docs/agencia_turismo.png).

## O que ele modela

O app se chama `fifacwc` e tem três models e quatro conjuntos de opções:

| Model | O que representa |
|-------|------------------|
| `Ingresso` | Titular, passaporte, data da compra, preço, estádio, setor, data do jogo, fase do torneio e cidade |
| `Passagem` | Código do voo, origem, destino, partida e chegada, titular, passaporte, preço e companhia aérea |
| `Pacote` | O responsável, e-mail, data da compra, preço total e forma de pagamento, ligando os ingressos e passagens vendidos juntos |

| Opções (`enumerations/`) | Valores |
|--------------------------|---------|
| `Fase` | Fase de grupos, oitavas, quartas, semifinal, final |
| `Setor` | Arquibancada, assento, cabine, área comum |
| `Pagamento` | Cartão de crédito, dinheiro, PIX |
| `Companhia` | Companhias aéreas |

A validação fica nos campos (tamanhos mínimos, valores mínimos como preço que não pode ser negativo, datas que não podem estar no passado) e no `BaseModel` compartilhado.

## Como rodar

Dá para explorar tudo pelo admin do Django:

```bash
cd agencia_turismo
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois abra `http://127.0.0.1:8000/admin/`. Usa SQLite e configurações de desenvolvimento (`DEBUG = True`), só para estudo local.

## O que aprendi

Transformar um diagrama UML em models, chaves estrangeiras e cardinalidade de relacionamentos (`0..1`, `0..*`), validadores de campo, enumerações com `TextChoices`, separar os models em um arquivo cada e ler as mensagens de erro do Django quando uma migração não bate com os models.

## Próximos passos

Ainda não há API nem telas próprias; este projeto é só a camada de dados. Também faltam testes automatizados (o arquivo `tests.py` é o modelo padrão).

> A `SECRET_KEY` do Django é lida da variável de ambiente `DJANGO_SECRET_KEY`. Se ela não estiver definida, é usada uma chave de desenvolvimento insegura, então nunca publique este projeto em produção como está.
