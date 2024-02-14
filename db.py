import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


db_user = os.getenv('DB_USER')
db_pw = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
conn_str = f'postgresql://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}'

def get_db_conn():
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn

def drop_events_table():
    try:
        # Get database connection
        conn = get_db_conn()
        cursor = conn.cursor()
        
        # Drop the events table if it exists
        drop_query = "DROP TABLE IF EXISTS events;"
        cursor.execute(drop_query)
        print("The 'events' table has been dropped.")
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.close()

if __name__ == '__main__':
    drop_events_table()