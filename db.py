from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST', 'mongodb')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'admin')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'secretpass')
MONGO_DB = os.getenv('MONGO_DB', 'threat_db')
MONGO_AUTH_SOURCE = os.getenv('MONGO_AUTH_SOURCE')

def client_connection():
    try:
        client = MongoClient(
            f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{int(MONGO_PORT)}"
            )
        return client
    except Exception as e:
        return Exception({'Error': str(e)})




def get_collection(client):
    db = client[MONGO_DB]
    collection = db[MONGO_DB]
    return collection

def save_documents(collection, df):
    collection.insert_many(df)