import sys
import os

from numpy import place
current = (os.path.dirname(os.path.realpath(__file__)))
parent = os.path.dirname(current)
sys.path.append(parent)
# Add path so that census_request and dbConfig
# can be imported

import census_request
import dbConfig
from datetime import date
from pymongo import MongoClient

# Gets the database
db = dbConfig.get_Database()
# gets the collection
cols = db['Socioeconomic']

def addInfo(fips, year=2019):

    # Function for adding a SINGLE record to the database
    # 
    # Includes:
    #     data: the dataset being entered 
    #     entry_time: the day, month and year when this entry took place
    #     fips: the FIPS code supplied to this function
    # 
    # returns True if the insertion was successful

    data = census_request.New_socioeconomic_census_api_request(fips)

    if not data:
        return False

    # Add the time that this was added so that the
    # record can be easily updated when the time comes
    entry_time = date.today()
    time = date.strftime(entry_time, '%m-%d-%Y')

    new_data = []
    for d in data:
        new_data.append(reKeyData(d))

    cols.insert_one(
    {
        'fips': fips,
        'timestamp': time,
        'dataset': new_data
    })

    return True

def getDataSet(fips):

    # Returns the entry in the database associated with the fips code

    data = cols.find(
        {'fips': fips}
    )
    r = []
    for i in data:
        r.append(i)
    return r


def updateData(fips, year=2019):
    
    # Used to update existing entries in the MongoDB
    # Does essentially the exact same thing as addInfo
    # except it updates instead of adds 

    data = census_request.Socioeconomic_census_api_request(fips, year)

    if not data:
        return False

    # Add the time that this was added so that the
    # record can be easily updated when the time comes
    entry_time = date.today()
    time = date.strftime(entry_time, '%m-%d-%Y')

    new_data = reKeyData(data)

    cols.update_one(
        {'fips': fips},
        {
            '$set':
            {'timestamp': time, 'dataset': new_data}
        }
    )

    return True


def reKeyData(data):

    new = getStringKeys()
    old = census_request.getSocioeconomicKeys()
    n = 0
    new_dict = {}
    for d in old:
        x = []
        for i in data[d]:
            x.append(i)
        new_dict[new[n]] = x
        n+=1
    return new_dict

def getStringKeys():
    new = (
       "Bachelor's degree or higher in labor force", "Bachelor's degree or higher", "Some college or associate's degree in labor force",
       "Some college or associate's degree", "High school graduate in labor force", "High school graduate", 
       "Less than high school graduate in labor force", "Less than high school graduate", "Total"
    )

    return new

