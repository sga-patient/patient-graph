import db.neo4jDB as neo4jDB
import db.neo4jController as neo4jController
import pandas as pd

def registerSymptom(filename):
    info = neo4jDB.getInfo()
    controller = neo4jController.Neo4jController(info["url"], info["user"], info["pw"])
    controller.connect("Hospital") # connect to neo4j

    # Get Data from CSV
    df = pd.read_csv(filename)

    print(df)
    
    subjects = df['2단계'].drop_duplicates().to_list()
    print(subjects)

    # register subject to neo4j
    for s in subjects:
        print(f"Create (m:Subject2" + "{" + f"subject: \"{s}\"" + "})")
        controller.run(f"Create (m:Subject2" + "{" + f"subject: \"{s}\"" + "})")
   
    symptoms = df[['2단계','4단계', '응급도 코드', '등급']]
    symptoms = symptoms.rename(columns={'2단계': '진료과', '4단계': '증상'})

    symptom = []
    for idx, val in symptoms.iterrows():
        symptom.append(val.to_dict())
    
    for s in symptom:
        print(f"Create (n:Symptom" + "{" + f"symptom: \"{s['증상']}\", subject: \"{s['진료과']}\", emergency_code: \"{s['응급도 코드']}\", level:{s['등급']}" + "})")
        controller.run(f"Create (n:Symptom" + "{" + f"symptom: \"{s['증상']}\", subject: \"{s['진료과']}\", emergency_code: \"{s['응급도 코드']}\", level:{s['등급']}" + "})")

    records, summary, keys = controller.driver.execute_query("MATCH(s:Subject2) RETURN s.subject as subject", database_='hospital')
    pathes = []
    for i in records:
        pathes.append(i['subject'])

    for path in pathes:
        print(path)
        r, s, k = controller.driver.execute_query("MATCH (s:Subject2{" + f"subject: \'{path}\'" + "}), (m:Symptom" + ") WHERE m.subject=\'" + f"{path}\'" + " CREATE (s)-[r:CLINIC4]->(m) RETURN s, type(r), m", database_='hospital')
        #r, s, k = controller.driver.execute_query(f"MATCH (s:Subject2 " + "{" + f"subject: \'{path}\'" + "})-[:CLINIC2]->(sym:Symptom" + "{subject: " + f"\'{path}\'" + "}" + ") RETURN s.subject, sym.symptom AS s, sym", database_='hospital')
        for i in r:
            print(i['s'], i['m'])

    '''
    with open(filename, 'r') as f:
        l = f.readline()
        lines = f.readlines()
        print(l)

        subjects = []
        for line in lines:
            symptoms = line.split(',')
            if '\"' in line:
                symptom = line.split('\"')[1]
                emer_code = symptoms[6]
            else:
                symptom = symptoms[4]
                emer_code = symptoms[5]

            #print(symptoms[0])
            subjects.append(symptoms[0])
            #controller.run(f"Create (n: Symptom " + "{" + f"symptom: \"{symptom}\", emergency_code: \"{emer_code}\", level:{symptoms[-1]}" + "})")
            
            #controller.run(f"Create path = (:Subject)-[:CLINIC]->(:Symptom) RETURN path limit 25")
        subject = tuple(subjects)
        for s in subject:
            controller.run(f"Create (m: Subject " + "{" + f"subject: \"{s}\"" + "})")
        '''

if __name__=="__main__":
    registerSymptom("data/응급환자_중증도_분류기준A.csv")