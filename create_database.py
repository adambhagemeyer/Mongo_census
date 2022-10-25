from http import client
import pymongo as mongo

DB_NAME = 'TDIdb'
CONNECTION_STRING = 'mongodb://127.0.0.1:27017/'

client = mongo.MongoClient(CONNECTION_STRING)

db = client[DB_NAME]
states_col = db["States"]
counties_col = db["Counties"]
occupation_col = db["OccupationByClassOfWorker"]
industry_col = db["IndustryByOccupation"]
education_col = db["Education"]
socio_col = db["Socioeconomic"]

def createStates():
    states_col.insert_many([
    {
        'state_name': 'Alabama',
        'state_code': '01'
    },
    {
        'state_name': 'Alaska',
        'state_code': '02'
    },
    {
        'state_name': 'Arizona',
        'state_code': '04'
    },
    {
        'state_name': 'Arkansas',
        'state_code': '05'
    },
    {
        'state_name': 'California',
        'state_code': '06'
    },
    {
        'state_name': 'Colorado',
        'state_code': '08'
    },
    {
        'state_name': 'Connecticut',
        'state_code': '09'
    },
    {
        'state_name': 'Delaware',
        'state_code': '10'
    },
    {
        'state_name': 'Washington DC',
        'state_code': '11'
    },
    {
        'state_name': 'Florida',
        'state_code': '12'
    },
    {
        'state_name': 'Georgia',
        'state_code': '13'
    },
    {
        'state_name': 'Hawaii',
        'state_code': '15'
    },
    {
        'state_name': 'Idaho',
        'state_code': '16'
    },
    {
        'state_name': 'Illinois',
        'state_code': '17'
    },
    {
        'state_name': 'Indiana',
        'state_code': '18'
    },
    {
        'state_name': 'Iowa',
        'state_code': '19'
    },
    {
        'state_name': 'Kansas',
        'state_code': '20'
    },
    {
        'state_name': 'Kentucky',
        'state_code': '21'
    },
    {
        'state_name': 'Louisiana',
        'state_code': '22'
    },
    {
        'state_name': 'Maine',
        'state_code': '23'
    },
    {
        'state_name': 'Maryland',
        'state_code': '24'
    },
    {
        'state_name': 'Massachusetts',
        'state_code': '25'
    },
    {
        'state_name': 'Michigan',
        'state_code': '26'
    },
    {
        'state_name': 'Minnesota',
        'state_code': '27'
    },
    {
        'state_name': 'Mississippi',
        'state_code': '28'
    },
    {
        'state_name': 'Missouri',
        'state_code': '29'
    },
    {
        'state_name': 'Montana',
        'state_code': '30'
    },
    {
        'state_name': 'Nebraska',
        'state_code': '31'
    },
    {
        'state_name': 'Nevada',
        'state_code': '32'
    },
    {
        'state_name': 'New Hampshire',
        'state_code': '33'
    },
    {
        'state_name': 'New Jersey',
        'state_code': '34'
    },
    {
        'state_name': 'New Mexico',
        'state_code': '35'
    },
    {
        'state_name': 'New York',
        'state_code': '36'
    },
    {
        'state_name': 'North Carolina',
        'state_code': '37'
    },
    {
        'state_name': 'North Dakota',
        'state_code': '38'
    },
    {
        'state_name': 'Ohio',
        'state_code': '39'
    },
    {
        'state_name': 'Oklahoma',
        'state_code': '40'
    },
    {
        'state_name': 'Oregon',
        'state_code': '41'
    },
    {
        'state_name': 'Pennsylvania',
        'state_code': '42'
    },
    {
        'state_name': 'Rhode Island',
        'state_code': '44'
    },
    {
        'state_name': 'South Carolina',
        'state_code': '45'
    },
    {
        'state_name': 'South Dakota',
        'state_code': '46'
    },
    {
        'state_name': 'Tennessee',
        'state_code': '47'
    },
    {
        'state_name': 'Texas',
        'state_code': '48'
    },
    {
        'state_name': 'Utah',
        'state_code': '49'
    },
    {
        'state_name': 'Vermont',
        'state_code': '50'
    },
    {
        'state_name': 'Virginia',
        'state_code': '51'
    },
    {
        'state_name': 'Washington',
        'state_code': '53'
    },
    {
        'state_name': 'West Virginia',
        'state_code': '54'
    },
    {
        'state_name': 'Wisconsin',
        'state_code': '55'
    },
    {
        'state_name': 'Wyoming',
        'state_code': '56'
    },
    {
        'state_name': 'Puerto Rico',
        'state_code': '72'
    }
    ])

    return True

def createCounties():

    content_list = ''
    with open('./counties.txt') as f:
        content_list = f.readlines()
    
    del content_list[0]

    for l in content_list:
        y = l.split()
        x = 4
        county_name = y[3]
        while not y[x].isnumeric():
            county_name += ' ' + y[x]
            x+=1
        counties_col.insert_one({
            'fips': y[1],
            'county_name': county_name,
            'state_code': y[1][:2]
        })

    return True

occupation_col = db['OccupationByClassOfWorker']
print('OccupationByClassOfWorker Created')
print('\n')
print('\n')
print('\n')
industry_col = db['IndustryByOccupation']
print('IndustryByOccupation Created')
print('\n')
print('\n')
print('\n')
education_col = db['Education']
print('Education Created')
print('\n')
print('\n')
print('\n')
socio_col = db['Socioeconomic']
print('Socioeconomic Created')
print('\n')
print('\n')
print('\n')
createStates()
print('States Created')
print('\n')
print('\n')
print('\n')
createCounties()
print('Counties Created')
print('\n')
print('\n')
print('\n')
print(f'DONE, {DB_NAME} CREATED')
