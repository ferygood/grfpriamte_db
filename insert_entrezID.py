import mysql.connector
import subprocess

def copy_csv_to_container(local_path, container_path):
    copy_command = f'docker cp {local_path} {container_path}'
    subprocess.run(copy_command, shell=True)
    print(f"File copied from {local_path} to {container_path}")

def load_csv_into_mysql(csv_file_path, db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Load CSV data into the primateGRFs table
        load_data_query = f"""
            LOAD DATA INFILE '{csv_file_path}' 
            INTO TABLE GRFID 
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"'
            LINES TERMINATED BY '\\n'
            IGNORE 1 ROWS;
        """

        cursor.execute(load_data_query)
        connection.commit()

        print("CSV data loaded into GRFID table successfully.")

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

    csv_file_path_local = './raw_data/EntrezEnsembl.csv'
    csv_file_path_container = 'mysql-container:/var/lib/mysql-files/EntrezEnsembl.csv'

    copy_csv_to_container(csv_file_path_local, csv_file_path_container)

    # Load CSV data into MySQL
    load_csv_into_mysql('/var/lib/mysql-files/EntrezEnsembl.csv', db_config)
