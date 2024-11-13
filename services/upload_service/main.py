from cassandra.cluster import Cluster
from fastapi import FastAPI

app = FastAPI()

@app.get('/upload/{file_path}')
async def upload_file(file_path: str):
    try:
        cluster = Cluster(["cassandra-service"])
        session = cluster.connect()
        session.set_keyspace('test_keyspace')

        session.execute("INSERT INTO test_table (list) VALUES (%s)", (file_path,))

        return {'Status': 'Upload Complete'}
        
    except Exception as e:
        return {'error': str(e)}
        