                MUSIC STORE MANAGEMENT SYSTEM

## Index
* [Jump to Database Schema](#database_Schema)
* [Jump to Files Planning](#files_Planning)

---
## database_Schema (MongoDB)

Collections:
    item = {
        '_id': 'ObjectId',
        'sku': SKU,
        'name': 'guitar',
        'category': '6 string guitar',
        'price': 'ProductPrice',
        'current_stock': 10,
        'unit': 'Pcs',
        'lead_time_days': 5,
        'min_safety_stock': 20
    },
    transaction = {
        '_id': 'ObjectId',
        'sku': '000000',   
        'type': 'OUT', // or 'IN'
        'quantity': 10,
        'timestamp': '2026-02-06T12:00:00Z',
        'user_id': 'user_01'
    },
    client = {
        'id': 'ObjectId',
        'cpf': 'Clientcpf',
        'name': 'ClientName',
        'phone': 'ClientPhone',
        'email': 'ClientEmail',
        'register_date': '2026-02-06T12:00:00Z'
    }

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