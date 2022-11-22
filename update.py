
#
# This is the script for updating the database
# As of now, this script will run every month
#

import dbConfig
import os
from datetime import date
from pymongo import MongoClient
import OccupationByClassOfWorker, Education, Socioeconomic, IndustryByOccupation

db = dbConfig.get_Database()

industry_cols = db['IndustryByOccupation']
occupation_cols = db['OccupationByClassOfWorker']
education_cols = db['Education']
socio_cols = db['Socioeconomic']

def update(fips):

    OccupationByClassOfWorker.updateData(fips)

    IndustryByOccupation.updateData(fips)

    Education.updateData(fips)

    Socioeconomic.updateData(fips)


n = 1
content_list = ''
with open('./counties.txt') as f:
    content_list = f.readlines()[n:]

x = n
for l in content_list:
    y = l.split()
    update(y[1])
    os.system('clear')
    if x != 0:
        prog = round((x / 3220) * 100, 4)
        print(f'Progress: {prog}%')
        print(f'Last added: {y[1]}')
        print('\n')
        print('\n')
    x+=1