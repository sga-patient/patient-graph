import db.neo4jDB as neo4jDB
import db.neo4jController as neo4jController

def registerSymptom(filename):
    info = neo4jDB.getInfo()
    controller = neo4jController.Neo4jController(info["url"], info["user"], info["pw"])
    controller.connect() # connect to neo4j

    with open(filename, 'r') as f:
        lines = f.readlines()
        print(lines)

if __name__=="__main__":
    registerSymptom("data/응급환자_중증도_분류기준A.csv")