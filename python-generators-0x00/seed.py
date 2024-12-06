"""
this code for  generators
"""

import mysql.connector
import uuid
import pandas as pd
def connect_db():
    """
    Function that connect sql server
    """
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    )
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS ALX_prodev')
    connection.commit()
    cursor.close()
def connect_to_prodev():
   return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ALX_prodev'
        )
def create_table(connection):
    """
    Fuction to create a table in database
    """
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data (
                   user_id VARCHAR(150) PRIMARY KEY,
                   name VARCHAR(150) NOT NULL,
                   email VARCHAR(150) NOT NULL,
                   age DECIMAL(5, 2) NOT NULL
            ) 
                   """)
    connection.commit()
    cursor.close()
def insert_data(connection, data):
    """
    Insert data from a CSV file into a database table.

    Args:
        connection: A MySQL database connection object.
        data_file: The path to the CSV file.
    """

    cursor = connection.cursor()

    data_df = pd.read_csv(data)

    for index, row in data_df.iterrows():
        user_id = str(uuid.uuid4())
        name = row['name']
        email = row['email']
        age = row['age']

        cursor.execute(
            """
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age)
            """,
            (user_id, name, email, age)
        )

    connection.commit()
    cursor.close()



