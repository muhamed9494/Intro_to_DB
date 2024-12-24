import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Function to create a database `alx_book_store` if it does not exist.
    """
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='159_753-Mo@fZ'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create the database
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()

    except Error as e:
        print(f"Error connecting to MySQL server: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
