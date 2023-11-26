import db.neo4jDB as neo4jDB
import db.neo4jController as neo4jController

def getInfoFromCsv(filename):
    info = neo4jDB.getInfo()
    controller = neo4jController.Neo4jController(info["url"], info["user"], info["pw"])
    controller.connect() # connect to neo4j

    hospitalList = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        idx = -1
        for line in lines:
            idx += 1
            if idx == 0:
                continue

            line = line.split(',')

            hospital = {}
            
            hospital["id"] = line[0]
            hospital["name"] = line[1]
            hospital["address"] = line[2]
            hospital["xy"] = {"alt": line[3], "long": line[4]}
            hospital["ph"] = line[5]
            hospital["beds"] = line[6]
            hospital["inpatient"] = line[7]
            hospital["dept"] = line[8]

            hospitalList.append(hospital)
    return hospitalList


if __name__=="__main__":
    filename = "/Volumes/Seagate/workspace/sga-patient/patient-graph/data/hospital.csv"

    getInfoFromCsv(filename)