import mysql.connector
print(mysql.connector.__version__)

print("Script is starting...")  
try:
    # Attempt to connect to the database
    conn = mysql.connector.connect(
        host="localhost",       # Replace with your host
        user="root",            # Replace with your username
        password="Arshiya@2307", # Replace with your password
        database="Bank_Sch",      # Replace with your database name (optional)
        auth_plugin="mysql_native_password" 
    )

    # Check if connection was successful
    if conn.is_connected():
        print("Connected to MySQL successfully!")
    else:
        print("Connection to MySQL failed.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection if it was successful
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")
