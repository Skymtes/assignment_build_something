from fastapi import FastAPI
from cassandra.cluster import Cluster

app = FastAPI()

@app.get("/")
async def root():
    try:
        cluster = Cluster(["cassandra-service"])
        session = cluster.connect()

        session.execute("""CREATE KEYSPACE if not exists test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};""")
        session.set_keyspace('test_keyspace')
        session.execute("""CREATE TABLE if not exists test_table (list text PRIMARY KEY);""")
        return {"message": "Welcome"}
    
    except Exception as e:
        return {'error': str(e)}