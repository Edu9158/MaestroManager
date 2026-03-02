from os import environ

class config():
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    MONGO_CONNECTION_URL = environ.get('MONGO_CONNECTION_URL')
