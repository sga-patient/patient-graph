import db.neo4jDB as neo4jDB
import db.neo4jController as neo4jController

def registerSymptom(filename):
    info = neo4jDB.getInfo()
    controller = neo4jController.Neo4jController(info["url"], info["user"], info["pw"])
    controller.connect("Hospital") # connect to neo4j

    with open(filename, 'r') as f:
        l = f.readline()
        lines = f.readlines()
        print(l)
        for line in lines:
            controller.run(f"MATCH (n: symptom " + "{" + f"symptom: {line.split(',')[4]}, emergency_code: {line.split(',')[6]}" + "})")
            controller.run(f"MATCH (m: subject " + "{" + f"subject: {line.split(',')[0]}" + "})")
            controller.run(f"CREATE ")

if __name__=="__main__":
    registerSymptom("data/응급환자_중증도_분류기준A.csv")