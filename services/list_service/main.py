from cassandra.cluster import Cluster
from fastapi import FastAPI

app = FastAPI()

@app.get('/list')
async def get_data():
    try: 
        cluster = Cluster(["cassandra-service"])
        session = cluster.connect()
        session.set_keyspace('test_keyspace')
        
        result = session.execute("SELECT * from test_table;")
        result_lst = []
        for rows in result:
            result_lst.append(rows)
            
        return {'content': result_lst}
    
    except Exception as e:
        return {'error': str(e)}
        
