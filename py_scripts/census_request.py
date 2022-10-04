import census
from datetime import date
import os
import dbConfig

db = dbConfig.get_Database()

states_col = db['States']
counties_col = db['Counties']
col = db['OccupationByClassOfWorker']


def census_api_request(code, param_year=date.today().year):
    ## Fetch the census api key
    c = census(os.getenv('CENSUS_API_KEY'))

    ## 
    dsource = 'pep'
    dname = 'components'
    cols = ''
    county = code[:2]
    state = code[-3:]
    year = str(param_year)
    ##

    base_url = 'https://api.census.gov/data/'
    dataset_url = f'{year}/{dsource}/{dname}/'




def getCounties(counties):

    if len(counties) == 0:
        return
    str = ''

    x = 1
    for i in counties:
        str += i[:2]
        if x <= len(counties):
            str += ','
        x+=1
    return str


