import Education
import Socioeconomic
import OccupationByClassOfWorker
import IndustryByOccupation
import dbConfig

def addToDB(fips):

    OccupationByClassOfWorker.addInfo(fips)

    IndustryByOccupation.addInfo(fips)

    Socioeconomic.addInfo(fips)

    Education.addInfo(fips)

    return True

def getFromDB(fips):
    occ = OccupationByClassOfWorker.getDataSet(fips)

    ind = IndustryByOccupation.getDataSet(fips)

    soc = Socioeconomic.getDataSet(fips)

    edu = Education.getDataSet(fips)

    return [occ, ind, soc, edu]

def updateDB(fips):
    occ = OccupationByClassOfWorker.updateData(fips)

    ind = IndustryByOccupation.updateData(fips)

    soc = Socioeconomic.updateData(fips)

    edu = Education.updateData(fips)

    return True

def checkDB(fips):

    db = dbConfig.get_Database()

    occ = db['OccupationByClassOfWorker']
    ind = db['IndustryByOccupation']
    soc = db['Socioeconomic']
    edu = db['Education']

    if occ.count_documents({'fips': fips}, limit=1) == 0:
        return False
    if ind.count_documents({'fips': fips}, limit=1) == 0:
        return False
    if soc.count_documents({'fips': fips}, limit=1) == 0:
        return False
    if edu.count_documents({'fips': fips}, limit=1) == 0:
        return False
    return True
