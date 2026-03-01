            MUSIC STORE MANAGEMENT SYSTEM (Maestro Manager)

## Index
* [Jump to Database Schema](#database_schema)
* [Jump to Files Planning](#files_planning)

---
## database_schema (MongoDB)
> MongoDB Atlas <-------------------------------------------------------

```python
# Just a model schema for mongo database collections.
#-------Collections-------
    product = {
        '_id': ObjectId(),
        'sku': 111111,
        'name': 'Guitar',
        'category': '6 string guitar',
        'color': 'red',
        'brand': 'ibanez',
        'price': 600.00,
        'weight': '5 kg',
        'current_stock': 10,
        'unit': 'Pçs',
        'load_date': "2026-02-27",
        'id_load': 1
    },{
        '_id': ObjectId(),
        'sku': 111112,
        'name': 'Bass',
        'category': '4 string bass',
        'color': 'spark red',
        'brand': 'ibanez',
        'price': 800.00,
        'weight': '6.5 kg',
        'current_stock': 8,
        'unit': 'Pçs',
        'load_date': "2026-02-27",
        'id_load': 1
    }

    load = {
        '_id': ObjectId(),
        'id_load': 1,
        'sku': 111111,
        'load_date': "2026-02-27",
        'placa': 'ABC-1234',
        'nom_fan': 'ABC FOODS LTDA',
        'raz_soc': 'ABC FOODS LTDA',
        'cnpj_cli': '00.000.000/0000-00',
        'cid_cli': 'ABC',
        'cep_cli': '11111-111',
        'address': "RUA ABC N 123",
        'total_load': 100,
        'unit': 'Pçs',
        'num_nfe': 123-456,
    }

    sale = {
        '_id': ObjectId(),
        'sale_id': 1,
        'items_sku': [
            {
                'product.sku': 111111,
                'product.price': 600.00, # Item 1 price
                'product.name':'Guitar'
            },{
                'product.sku': 111112,
                'product.price': 800.00, # Item 2 price
                'product.name':'Bass'
            }
        ],
        'sale_price': 1400.00, # (item 1 + item 2)
        'quantity': 1,
        'sale_date': "2026-02-27",
        'user_id': 1,
        'client_id': 1
    }

    client = {
        '_id': ObjectId(),
        'client_id': 1,
        'cpf': '000.000.000-00', # Could be a CNPJ
        'name': 'José',
        'phone': '+554400000000',
        'email': 'fictitious@email.com',
        'register_date': "2026-02-27"
    }

    user = {
        '_id': ObjectId(),
        'user_id': 1,
        'cpf': '000.000.000-00', 
        'name': 'Flavinho',
        'phone': '+554400000000',
        'email': 'fictitious@email.com',
        'register_date': "2026-02-27"
    }
```

---
## files_Planning

smart_inventory/
├── app.py              # The "Main" entry point
├── requirements.txt    # Your library list
├── .env                # Secret keys (DB URL, Token secrets)
├── .gitignore          # Ignore venv/, .env, and __pycache__
├── core/               # The "Brain" (Business Logic)
│   ├── __init__.py
│   ├── inventory.py    # Logic for ROP, stock calculations
│   └── auth.py         # Logic for login and tokens
├── routes/             # The "Voice" (API Endpoints)
│   ├── __init__.py
│   ├── tracking.py     # Flask Blueprints for stock moves
│   └── users.py        # Blueprints for user management
├── database/           # The "Memory" (Connection logic)
│   ├── __init__.py
│   └── mongo_client.py # Global MongoDB connection
└── tests/              # The "Insurance" (Pytest)
    ├── conftest.py
    └── test_inventory.py       

---
## 