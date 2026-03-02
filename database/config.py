import os
from dotenv import load_dotenv

load_dotenv()

class config():
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    MONGO_CONNECTION_URL = os.environ.get('MONGO_CONNECTION_URL')
