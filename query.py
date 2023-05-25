import psycopg

with psycopg.connect("dbname=tfprimate user=postgres password=yao123") as conn:
    
    with conn.cursor() as cur:
        cur.execute(
            "SELECT EnsemblID, GeneName FROM primategrfs;"
        )

        results = cur.fetchall()

        conn.commit()

print(f"Query results are {results}")