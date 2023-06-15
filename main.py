from fastapi import FastAPI
from typing import Union
import psycopg
from psycopg import sql

app = FastAPI()

# Connect to the PostgreSQL database
# with psycopg.connect("""
#      host=localhost 
#      port=5432 
#      dbname=tfprimate 
#      user=postgres 
#      password=yao123
#      """) as conn:
    
#     cur = conn.cursor()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @app.get("/alignment")
# def get_alignment():
#     cur.execute("SELECT * FROM alignment")
#     alignment_data = cur.fetchall()
#     return {"alignment": alignment_data}

# @app.get("/grfid")
# def get_grfid():
#     cur.execute("SELECT * FROM grfid")
#     grfid_data = cur.fetchall()
#     return {"grfid": grfid_data}

# @app.get("/grfsannotation")
# def get_grfsannotation():
#     cur.execute("SELECT * FROM grfsannotation")
#     grfsannotation_data = cur.fetchall()
#     return {"grfsannotation": grfsannotation_data}

# @app.get("/primategrfs")
# def get_primategrfs():
#     cur.execute("SELECT * FROM primategrfs")
#     primategrfs_data = cur.fetchall()
#     return {"primategrfs": primategrfs_data}

# # Close the cursor and connection when the application stops
# @app.on_event("shutdown")
# def shutdown_event():
#     cur.close()
#     conn.close()
