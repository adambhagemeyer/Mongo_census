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
cols = db['Education']

def addInfo(fips, year=2019):

    # Function for adding a SINGLE record to the database
    # 
    # Includes:
    #     data: the dataset being entered 
    #     entry_time: the day, month and year when this entry took place
    #     fips: the FIPS code supplied to this function
    # 
    # returns True if the insertion was successful

    data = census_request.Education_census_api_request(fips, year)

    # Check to ensure that the census request returned the data
    if not data:
        return False
        
    # Add the time that this was added so that the
    # record can be easily updated when the time comes
    entry_time = date.today()
    time = date.strftime(entry_time, '%m-%d-%Y')

    new_data = reKeyData(data)

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

    data = census_request.Education_census_api_request(fips, year)

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
    old = census_request.getEducationKeys()
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
    # "B15003_001","Total"
    # "B15003_002","No Schooling Completed"
    # "B15003_003","Nursery School"
    # "B15003_004","Kindergarten"
    # "B15003_005","1st grade"
    # "B15003_006","2nd grade"
    # "B15003_007","3rd grade"
    # "B15003_008","4th grade"
    # "B15003_009","5th grade"
    # "B15003_010","6th grade"
    # "B15003_011","7th grade"
    # "B15003_012","8th grade"
    # "B15003_013","9th grade"
    # "B15003_014","10th grade"
    # "B15003_015","11th grade"
    # "B15003_016","12th grade, no diploma"
    # "B15003_017","Regular high school diploma"
    # "B15003_018","GED or alternative credential"
    # "B15003_019","Some college, less than 1 year"
    # "B15003_020","Some college, 1 or more years, no degree"
    # "B15003_021","Associate's degree"
    # "B15003_022","Bachelor's degree"
    # "B15003_023","Master's degree"
    # "B15003_024","Professional school degree"
    # "B15003_025","Doctorate degree"
    new = (
       "Doctorate degree", "Professional school degree", "Master's degree", "Bachelor's degree",
       "Associate's degree", "Some college, 1 or more years, no degree", "Some college, less than 1 year",
       "GED or alternative credential", "Regular high school diploma", "12th grade, no diploma", 
       "11th grade", "10th grade", "9th grade", "8th grade", "7th grade", "6th grade", "5th grade", 
       "4th grade", "3rd grade", "2nd grade", "1st grade", "Kindergarten", "Nursery School", "No Schooling Completed",
       "Total"
    )

    return new