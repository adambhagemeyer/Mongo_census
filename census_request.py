
# Python functions for returning data from the census API. 
# Contains one function for each of the 4 tables that are 
# used in TDI 
# NOTE: Testing shows that running all 4 one after another
# will take roughly 16 seconds

from email.errors import ObsoleteHeaderDefect
from census import Census
from datetime import date
import os
import dbConfig

db = dbConfig.get_Database()

states_col = db['States']
counties_col = db['Counties']

## Pull Occupation data from the Census API
def Occupation_census_api_request(code, param_year=2019):
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    # What do the codes pull:
    # "C24060_001","Total"
    # "C24060_002","Management, business, science, and arts occupations"
    # "C24060_003","Service occupations"
    # "C24060_004","Sales and office occupations"
    # "C24060_005","Natural resources, construction, and maintenance occupations"
    # "C24060_006","Production, transportation, and material moving occupations"
    cols = (
        'C24060_006E', 'C24060_005E', 'C24060_004E', 'C24060_003E', 'C24060_002E', 'C24060_001E'
        )
    # County Code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State Code: First 2 digits of the FIPS code
    state = code[:2]

    ## API call 
    data = c.acs5.state_county(fields = cols, 
                                state_fips=state, county_fips=county, year=param_year)

    ## Return the data in JSON format
    return data


## Pull Industry data from the Census API
def Industry_census_api_request(code, param_year=2019): 
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    # What do the codes pull:
    # "C24050_001","Total"
    # "C24050_002","Agriculture, forestry, fishing and hunting, and mining"
    # "C24050_003","Construction"
    # "C24050_004","Manufacturing"
    # "C24050_005","Wholesale trade"
    # "C24050_006","Retail trade"
    # "C24050_007","Transportation and warehousing, and utilities"
    # "C24050_008","Information"
    # "C24050_009","Finance and insurance, and real estate, and rental and leasing"
    # "C24050_010","Professional, scientific, and management, and administrative, and waste management services"
    # "C24050_011","Educational services, and health care and social assistance"
    # "C24050_012","Arts, entertainment, and recreation, and accommodation and food services"
    # "C24050_013","Other services, except public administration"
    # "C24050_014","Public administration"
    cols = (
        'C24050_014E', 'C24050_013E', 'C24050_012E', 'C24050_011E', 'C24050_010E', 
        'C24050_009E', 'C24050_008E', 'C24050_007E', 'C24050_006E', 'C24050_005E',
        'C24050_004E', 'C24050_003E', 'C24050_002E', 'C24050_001E'
    )
    # County code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State code: First 2 digits of the FIPS code
    state = code[:2]
    
    ## API call
    data = c.acs5.state_county(fields = cols, 
                               state_fips=state, county_fips=county, year=param_year)

    ## Return that data in JSON format
    return data


## Pull Education data from the Census API
def Education_census_api_request(code, param_year=2019): 
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    # What do the codes pull: 
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
    cols = (
        'B15003_025E', 'B15003_024E', 'B15003_023E', 'B15003_022E', 'B15003_021E',
        'B15003_020E', 'B15003_019E', 'B15003_018E', 'B15003_017E', 'B15003_016E',
        'B15003_015E', 'B15003_014E', 'B15003_013E', 'B15003_012E', 'B15003_011E',
        'B15003_010E', 'B15003_009E', 'B15003_008E', 'B15003_007E', 'B15003_006E',
        'B15003_005E', 'B15003_004E', 'B15003_003E', 'B15003_002E', 'B15003_001E'
    )
    # County code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State code: First 2 digits of the FIPS code
    state = code[:2]

    ## API call
    data = c.acs5.state_county(fields = cols, 
                               state_fips=state, county_fips=county, year=param_year)

    ## Return that data in JSON format
    return data


## Pull Socioeconomic data using the census API
def Socioeconomic_census_api_request(code, param_year=2019):
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    # What do the codes pull:
    # "B23006_001","Total"
    # "B23006_002","Less than high school graduate"
    # "B23006_003","Less than high school graduate in labor force"
    # "B23006_009","High school graduate"
    # "B23006_010","High school graduate in labor force"
    # "B23006_016","Some college or associate's degree"
    # "B23006_017","Some college or associate's degree in labor force"
    # "B23006_023","Bachelor's degree or higher"
    # "B23006_024","Bachelor's degree or higher in labor force"
    cols = (
        'B23006_024E', 'B23006_023E', 'B23006_017E', 'B23006_016E', 'B23006_010E',
        'B23006_009E', 'B23006_003E', 'B23006_002E', 'B23006_001E'
    )
    # County Code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State Code: First 2 digits of the FIPS code
    state = code[:2]

    ## API call
    data = c.acs5.state_county(fields=cols,
                                state_fips=state, county_fips=county, year=param_year)

    ## Return the data in JSON format
    return data
