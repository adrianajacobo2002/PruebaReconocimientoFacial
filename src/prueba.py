import mysql.connector
from mysql.connector import Error
import json

def get_db_config():
    with open('keys.json', 'r') as file:
        config = json.load(file)
    return config

def check_database_connection():
    config = get_db_config()
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        if connection.is_connected():
            print("Connection to database was successful!")
            connection.close()
            return True
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return False

if __name__ == "__main__":
    if check_database_connection():
        print("Connection to database verified.")
    else:
        print("Failed to connect to database.")
