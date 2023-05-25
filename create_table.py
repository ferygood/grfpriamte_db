import psycopg

with psycopg.connect("dbname=tfprimate user=postgres password=yao123") as conn:
    
    # create primate GRFs table
    with conn.cursor() as cur:
      cur.execute("""
        CREATE TABLE IF NOT EXISTS primateGRFs(
          EnsemblID varchar(50) primary key,
          GeneName varchar(10),
          Hsap varchar(50),
          Anan varchar(50),
          Capa varchar(50),
          Caty varchar(50),
          Ccap varchar(50),
          Cjac varchar(50),
          Csab varchar(50),
          Ggor varchar(50),
          Mfas varchar(50),
          Mleu varchar(50),
          Mmul varchar(50),
          Mmur varchar(50),
          Mnem varchar(50),
          Nleu varchar(50),
          Ogar varchar(50),
          Ppyg varchar(50),
          Panu varchar(50),
          Pcoq varchar(50),
          Ppan varchar(50),
          Psim varchar(50),
          Ptep varchar(50),
          Ptro varchar(50),
          Rbie varchar(50),
          Rrox varchar(50),
          Sbbo varchar(50),
          Tgel varchar(50),
          Tsyr varchar(50),
          numNA INT
        );
      """)
    
    conn.commit()