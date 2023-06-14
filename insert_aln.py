#an example how to insert alignment sequence
#need ortholog alignments?
#allow TFs without ortholog information?
#main ortholog table does not have example, ELOA3PD

import psycopg
from psycopg import sql

# read fasta in plain text
fasta_file = "./raw_data/ENSG00000288616_codon.fa"

# Read the contents of the FASTA file
with open(fasta_file, "r") as file:
    fasta_string = file.read()

# insert into alignment table
with psycopg.connect("""
     host=localhost 
     port=5432 
     dbname=tfprimate 
     user=postgres 
     password=yao123
     """) as conn:
    
    with conn.cursor() as cur:
        cur.execute(
            sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s)")
              .format(sql.Identifier('alignment')),
              ["ENSG00000288616", "ELOA3DP", fasta_string, "fasta"]
        )
        
        conn.commit()


      