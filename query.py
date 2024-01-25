import mysql.connector

db_config = {
        'host': '172.17.0.2',
        'user': 'root',
        'password': 'yao123',
        'database': 'grfprimate',
    }

with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT EnsemblID, GeneName FROM primateGRFs;")
        results = cursor.fetchall()

print(f"Query results are {results}")
