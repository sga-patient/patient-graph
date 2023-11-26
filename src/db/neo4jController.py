class Neo4jController:
    def __init__(self, url, user, pw):
        self.url = url
        self.user = user
        self.pw = pw
        self.session = None

    def connect(self):
        from neo4j import GraphDatabase

        if self.session == None:
            driver = GraphDatabase.driver(self.url, auth=(self.user, self.pw))
            self.session = driver.session()
    
    def run(self, q):
        self.session.run(q)
    
    def close(self):
        if self.session == None:
            return
        self.session.close()

    def selectAll(self):
        q = "MATCH (n) RETURN n"
        nodes = self.run(q)

        for node in nodes:
            print(node)