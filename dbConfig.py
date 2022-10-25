from pymongo import MongoClient


CONNECTION_STRING = 'mongodb://127.0.0.1:27017/'
DB_NAME = 'TDIdb'

def get_Database():
    client = MongoClient(CONNECTION_STRING)
    return client[DB_NAME]
