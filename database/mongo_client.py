"""
Database connection module.
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import config

class DB(object):
    """
    Stablishes a DB instance.
    """
    url = config.MONGO_CONNECTION_URL

    # Create a new client and connect to the server
    client = MongoClient(url, server_api = ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as error:
        print(error)

    #def get_mongo_client():
    #def get_data():
