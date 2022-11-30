from pymongo import MongoClient


CONNECTION_STRING = 'mongodb://TDI:TDIaccount@cpsc4910-mysql11.research.utc.edu:27017/'
DB_NAME = 'TDIdb'

def get_Database():
    client = MongoClient(CONNECTION_STRING+DB_NAME)
    return client[DB_NAME]
