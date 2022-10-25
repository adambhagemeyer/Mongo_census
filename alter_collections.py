import Education
import Socioeconomic
import OccupationByClassOfWorker
import IndustryByOccupation

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
