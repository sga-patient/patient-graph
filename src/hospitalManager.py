import db.neo4jDB as neo4jDB
import db.neo4jController as neo4jController

def putInDB(filename):
    info = neo4jDB.getInfo()
    controller = neo4jController.Neo4jController(info["url"], info["user"], info["pw"])
    controller.connect()

    with open(filename, 'r') as f:
        lines = f.readlines()
        print(lines)


if __name__=="__main__":
    filename = "/Volumes/Seagate/workspace/sga-patient/patient-graph/data/hospital.csv"

    putInDB(filename)