from pymongo import MongoClient
import os



MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DB = os.getenv('MONGO_DB')
MONGO_AUTH_SOURCE = os.getenv('MONGO_AUTH_SOURCE')

def client_connection():
    try:
        client = MongoClient(
            f'{MONGO_HOST}://{MONGO_USERNAME}:{MONGO_PORT}/'
        )
        return client
    except Exception as e:
        return Exception(str(e))


def get_collection(client):
    db = client[MONGO_DB]
    collection = db[MONGO_DB]
    return collection


def save_documents(collection, df):
    collection.insert_many(df)