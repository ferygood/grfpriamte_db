import psycopg

with psycopg.connect("""
     host=localhost 
     port=5432 
     dbname=tfprimate 
     user=postgres 
     password=yao123
     """) as conn:
    
    # create primate GRFs table
    with conn.cursor() as cur:
      cur.execute("""
        CREATE TABLE IF NOT EXISTS primateGRFs(
          EnsemblID varchar(50) primary key,
          GeneName varchar(30),
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

      # create julias table
      cur.execute("""
        CREATE TABLE IF NOT EXISTS GRFsAnnotation(
          GRF varchar(50),
          GeneName varchar(30),
          EnsemblID varchar(50) primary key,
          GeneSynonyms varchar(50),
          ChromosomeLocation text,
          TFCatID varchar(20),
          FunctionClass text,
          NCBIRefSeqID varchar(30),
          TFClass varchar(30),
          HTFDBID text,
          DBD text,
          IsTF varchar(30),
          TFAssessment text,
          BindingMode text,
          MotifStatus text,
          Notes text,
          FOREIGN KEY (EnsemblID) REFERENCES primateGRFs(EnsemblID)
        );
      """)

      # create alignment table
      cur.execute("""
        CREATE TABLE IF NOT EXISTS Alignment(
          EnsemblID varchar(50) primary key,
          GeneName varchar(30),
          Content text,
          Format varchar(10),
          FOREIGN KEY (EnsemblID) REFERENCES primateGRFs(EnsemblID)
        );
      """)

      # create entrezid table
      cur.execute("""
        CREATE TABLE IF NOT EXISTS GRFID(
          EnsemblID varchar(50) primary key,
          Entrezid varchar(50),
          GeneName varchar(30),
          FOREIGN KEY (EnsemblID) REFERENCES primateGRFs(EnsemblID)
        );
      """)
    
    conn.commit()