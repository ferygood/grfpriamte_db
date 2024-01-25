#an example how to insert alignment sequence
#need ortholog alignments?
#allow TFs without ortholog information?
#main ortholog table does not have example, ELOA3PD

import mysql.connector

def insert_alignment_data(ensembl_id, gene_name, fasta_content, format, db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert into the alignment table
        insert_query = """
            INSERT INTO Alignment (EnsemblID, GeneName, Content, Format)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (ensembl_id, gene_name, fasta_content, format))
        connection.commit()

        print("Alignment data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    
    db_config = {
        'host': '172.17.0.2',
        'user': 'root',
        'password': 'yao123',
        'database': 'grfprimate',
    }

    fasta_file_path_local = './raw_data/ENSG00000288616_codon.fa'

    # Read the contents of the FASTA file
    with open(fasta_file_path_local, "r") as file:
        fasta_string = file.read()

    # Insert alignment data into MySQL
    insert_alignment_data('ENSG00000288616', 'ELOA3DP', fasta_string, 'fasta', db_config)
