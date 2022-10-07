from sys import get_coroutine_origin_tracking_depth
import dbConfig

db = dbConfig.get_Database()
states_col = db['States']
counties_col = db['Counties']
 
## Returns all counties queried according to the state FIPS code
def getCountiesByStateName(state_name):
    state_code = states_col.find_one(
        {'state_name': state_name})['state_code']
    counties = [doc['county_name'] for doc in counties_col.find({ 'state_code': state_code })]

    return counties

## Returns all counties queried according to the state FIPS code
def getCountiesByStateCode(state_code):
    return [doc['county_name'] for doc in counties_col.find({ 'state_code': state_code })]


# testing
# code_or_state = input("Are you entering a state name? (y/n): ")

# if code_or_state == 'y':
#     state = input('State Name: ')
#     print(getCountiesByStateName(state))

# else:
#     code = input('State Code: ')
#     print(getCountiesByStateCode(code))


