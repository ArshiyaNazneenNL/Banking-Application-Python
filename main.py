def main_menu():
    print("Welcome to the Banking Application")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register_user()
    elif choice == 2:
        login_user()
    elif choice == 3:
        print("Thank you for using the application!")
    else:
        print("Invalid choice!")


from db_connection import get_db_connection
from utils import generate_card_number
import random

def register_user():
    print("\n--- Register User ---")
    username = input("Enter your name: ")
    address = input("Enter your address: ")
    aadhar = input("Enter your Aadhar number: ")
    mobile = input("Enter your mobile number: ")

    # Generate cards
    credit_card = generate_card_number()
    debit_card = generate_card_number()
    credit_card_pin = str(random.randint(1000, 9999))
    debit_card_pin = str(random.randint(1000, 9999))
    credit_card_cvv = str(random.randint(100, 999))
    debit_card_cvv = str(random.randint(100, 999))

    # Insert into database
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO users (username, address, aadhar, mobile, credit_card, debit_card)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, address, aadhar, mobile, credit_card, debit_card))
        connection.commit()
        print("\nUser registered successfully!")
        print(f"Credit Card: {credit_card}, PIN: {credit_card_pin}, CVV: {credit_card_cvv}")
        print(f"Debit Card: {debit_card}, PIN: {debit_card_pin}, CVV: {debit_card_cvv}")
    except Exception as e:
        print("Error occurred during registration:", e)
    finally:
        connection.close()


from db_connection import get_db_connection

def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    mobile = input("Enter your mobile number: ")

    # Verify user credentials
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND mobile = %s"
        cursor.execute(query, (username, mobile))
        user = cursor.fetchone()
        if user:
            print("\nLogin successful!")
            print(f"Welcome, {user[1]}!")  # Assuming username is in the second column
            # You can add logic here to navigate to the main menu after login
        else:
            print("Invalid username or mobile number. Please try again.")
    except Exception as e:
        print("Error occurred during login:", e)
    finally:
        connection.close()
