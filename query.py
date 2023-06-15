import psycopg
from psycopg import sql

with psycopg.connect("""
     host=localhost 
     port=5432 
     dbname=tfprimate 
     user=postgres 
     password=yao123
     """) as conn:
    
    with conn.cursor() as cur:
        cur.execute(
            sql.SQL("""
            SELECT * FROM GRFID LIMIT 5;
        """))
                
        results = cur.fetchall()  
        conn.commit()

print(f"Query results are {results}")