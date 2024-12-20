import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arshiya@2307",
        database="banking_app"
    )
    return connection
