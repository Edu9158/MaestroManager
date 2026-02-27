                MUSIC STORE MANAGEMENT SYSTEM

## Index
* [Jump to Database Schema](#database_Schema)
* [Jump to Files Planning](#files_Planning)

---
## database_Schema (MongoDB)

```python
#-------Collections-------
    item = {
        '_id': ObjectId(),
        'sku': 111111,
        'name': 'Guitar',
        'category': '6 string guitar',
        'color': 'red',
        'brand': 'ibanez',
        'price': 600.00,
        'current_Stock': 10,
        'unit': 'Pçs',
        'load_Date': "2026-02-27",
        'id_Load': 111,
    }

    load = {
        '_id': ObjectId(),
        'id_Load': 111,
        'load_Date': "2026-02-27",
        'placa': 'ABC-1234',
        'sequency': 2,
        'status': 1,
        'idorca': 5,
        'nomfan': 'ABC FOODS LTDA',
        'razdoc': 'ABC FOODS LTDA',
        'cnpjcl': '00.000.000/0000-00',
        'cidcli': 'ABC',
        'cepcli': '11111-111',
        'endereco': "RUA ABC N 123",
        'idenit': 1,
        'qtdent': 100,
        'idprod': test_products[0]['idprod'],
        'numnfe': '',
        'syncDate': datetime.now(timezone.utc),
    }

    nfe = {
        
    }

    transaction = {
        '_id': ObjectId(),
        'sku': 111111,   
        'type': 'OUT', // or 'IN'
        'quantity': 10,
        'timestamp': '2026-02-06T12:00:00Z',
        'user_id': 'user_01'
    }

    client = {
        '_id': ObjectId(),
        'cpf': 'Clientcpf',
        'name': 'ClientName',
        'phone': 'ClientPhone',
        'email': 'ClientEmail',
        'register_date': '2026-02-06T12:00:00Z'
    }

    user = {
        '_id': ObjectId(),
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