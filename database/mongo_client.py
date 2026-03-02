"""
Database connection module.
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from os import environ

class DB(object):

    APP_NAME = ''







MONGO_0_CONNECTION_URL 

uri = 

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as error:
    print(error)