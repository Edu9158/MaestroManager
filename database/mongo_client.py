"""
Database connection module.
"""
from config import config
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class DB(object):
    """
    Stablishes a DB instance.
    """
    uri = config.MONGO_CONNECTION_URL
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api = ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as error:
        print(error)

    db = client.mm_DB1

    #def get_database():
    #def get_data():

    def insert_one_document(self, product, data):
        """
        Insere um único documento em uma coleção específica do MaestroManager.
        """
        
        collection = db.product
        
        result = collection.insert_one(data)
        
        return result.inserted_id

    
    if __name__ == "__main__":
        print("Iniciando o teste de inserção no Atlas...")
        
        # 1. Criamos a nossa folha de papel (O dicionário Python)
        data = {
            "sku": "GTR-PRO-001",
            "name": "Fender Stratocaster Profissional",
            "price": 1500.00,
            "color": "Sunburst",
            "strings": 6
        }
        
        # 2. Entregamos para a NOSSA função guardar na gaveta "products"
        try:
            novo_id = insert_one_document("product", data)
            print(f"✅ SUCESSO TOTAL! A guitarra foi salva no Atlas com o ID: {novo_id}")
        except Exception as e:
            print(f"❌ Ops, algo deu errado: {e}")






    #def insert_many():

    #def update_document():
    #def update_stock():

    #def delete_document():