
# Python functions for returning data from the census API. 
# Contains one function for each of the 4 tables that are 
# used in TDI 
# NOTE: Testing shows that running all 4 one after another
# will take roughly 16 seconds

from curses import use_default_colors
from email.errors import ObsoleteHeaderDefect
from census import Census
from datetime import date
import os
import dbConfig

## Pull Occupation data from the Census API
def Occupation_census_api_request(code, param_year=2019):
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    cols = getOccupationKeys()
    # County Code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State Code: First 2 digits of the FIPS code
    state = code[:2]

    totals_cols = append_in_list(cols, 'E')
    percentage_cols = append_in_list(cols, 'M')

    ## API call
    totals_data = c.acs5.state_county(fields = totals_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    percentage_data = c.acs5.state_county(fields = percentage_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    if not totals_data and not percentage_data:
        return {}

    data = combine_data_sets(totals_data, percentage_data, cols)
    
    ## Return the data in JSON format
    return data


## Pull Industry data from the Census API
def Industry_census_api_request(code, param_year=2019): 
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    cols = getIndustryKeys()
    # County code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State code: First 2 digits of the FIPS code
    state = code[:2]
    
    totals_cols = append_in_list(cols, 'E')
    percentage_cols = append_in_list(cols, 'M')

    ## API call
    totals_data = c.acs5.state_county(fields = totals_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    percentage_data = c.acs5.state_county(fields = percentage_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    if not totals_data or not percentage_data:
        return {}

    data = combine_data_sets(totals_data, percentage_data, cols)

    ## Return that data in JSON format
    return data


## Pull Education data from the Census API
def Education_census_api_request(code, param_year=2019): 
    ## Fetch the census api key
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    cols = getEducationKeys()
    # County code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State code: First 2 digits of the FIPS code
    state = code[:2]

    totals_cols = append_in_list(cols, 'E')
    percentage_cols = append_in_list(cols, 'M')

    ## API call
    totals_data = c.acs5.state_county(fields = totals_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    percentage_data = c.acs5.state_county(fields = percentage_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    if not totals_data or not percentage_data:
        return {}

    data = combine_data_sets(totals_data, percentage_data, cols)
    
    ## Return that data in JSON format
    return data


## Pull Socioeconomic data using the census API
def Socioeconomic_census_api_request(code, param_year=2019):
    API_KEY = 'd19843a72adf95bac43d31835bbd3af890e80a86'
    c = Census(API_KEY)

    cols = getSocioeconomicKeys()
    # County Code: Last 3 digits of the FIPS code
    county = code[-3:]
    # State Code: First 2 digits of the FIPS code
    state = code[:2]

    totals_cols = append_in_list(cols, 'E')
    percentage_cols = append_in_list(cols, 'M')

    ## API call
    totals_data = c.acs5.state_county(fields = totals_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    percentage_data = c.acs5.state_county(fields = percentage_cols, 
                               state_fips=state, county_fips=county, year=param_year)

    if not totals_data or not percentage_data:
        return {}

    data = combine_data_sets(totals_data, percentage_data, cols)
    
    ## Return the data in JSON format
    return data

# Returns the columns that will be used in the Occupation API request
def getOccupationKeys():

    # What do the codes pull:
    # "C24060_001","Total"
    # "C24060_002","Management, business, science, and arts occupations"
    # "C24060_003","Service occupations"
    # "C24060_004","Sales and office occupations"
    # "C24060_005","Natural resources, construction, and maintenance occupations"
    # "C24060_006","Production, transportation, and material moving occupations"
    cols = [
        'C24060_006', 'C24060_005', 'C24060_004', 'C24060_003', 'C24060_002', 'C24060_001'
    ]
    
    return cols

# Returns the columns that will be used in the Industry API request
def getIndustryKeys():

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
    cols = [
        'C24050_014', 'C24050_013', 'C24050_012', 'C24050_011', 'C24050_010', 
        'C24050_009', 'C24050_008', 'C24050_007', 'C24050_006', 'C24050_005',
        'C24050_004', 'C24050_003', 'C24050_002', 'C24050_001'
    ]

    return cols

# Returns the columns that will be used in the Education API request
def getEducationKeys():
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
    cols = [
        'B15003_025', 'B15003_024', 'B15003_023', 'B15003_022', 'B15003_021',
        'B15003_020', 'B15003_019', 'B15003_018', 'B15003_017', 'B15003_016',
        'B15003_015', 'B15003_014', 'B15003_013', 'B15003_012', 'B15003_011',
        'B15003_010', 'B15003_009', 'B15003_008', 'B15003_007', 'B15003_006',
        'B15003_005', 'B15003_004', 'B15003_003', 'B15003_002', 'B15003_001'
    ]

    return cols

# Returns the columns that will be used in the Socioeconomic API request
def getSocioeconomicKeys():

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
    cols = [
        'B23006_024', 'B23006_023', 'B23006_017', 'B23006_016', 'B23006_010',
        'B23006_009', 'B23006_003', 'B23006_002', 'B23006_001'
    ]

    return cols

# Adds the key specifier to the end of the keys use
# in the census api 
def append_in_list(data, suffix):
    return [x + suffix for x in data]


def combine_data_sets(new, old, keys):
    newlistkeys = append_in_list(keys, 'E')
    oldlistkeys = append_in_list(keys, 'M')

    newdict = {}
    x = 0
    for k in keys:
        pct = round(new[0][newlistkeys[x]] / new[0][newlistkeys[last_index(newlistkeys)]], 2)
        newdict[k] = [new[0][newlistkeys[x]], old[0][oldlistkeys[x]], pct] 
        x+=1

    return newdict

def last_index(l):
    return len(l)-1
