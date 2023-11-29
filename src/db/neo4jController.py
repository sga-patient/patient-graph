class Neo4jController:
    def __init__(self, url, user, pw):
        self.url = url
        self.user = user
        self.pw = pw
        self.session = None
        self.driver = None

    def connect(self, database="neo4j"):
        from neo4j import GraphDatabase

        if self.session == None:
            self.driver = GraphDatabase.driver(self.url, auth=(self.user, self.pw))
            self.session = self.driver.session(database=database)
    
    def run(self, q):
        self.session.run(q)
    
    def close(self):
        if self.session == None:
            return
        self.session.close()
        self.driver.close()

    def selectAll(self, database="neo4j"):
        q = f"MATCH (n: {database}) RETURN n"
        nodes = self.run(q)

        if nodes == None:
            print('None')
            return

        for node in nodes:
            print(node)