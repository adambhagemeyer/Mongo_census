from pymongo import MongoClient
import time
import dbConfig

db = dbConfig.get_Database()
states_col = db['States']

## Returns a list of the names of the states and territories in the db
def getStateNames():
    states = [doc['state_name'] for doc in states_col.find()]
    return states

def getStateFips():
    fips = [doc['state_code'] for doc in states_col.find()]
    return fips

