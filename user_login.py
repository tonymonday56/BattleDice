#user_login.py
# user database to store registered users
import sqlite3
user_database = {}

def register_user(username, password):
    """
    Function to register a new user
    """
    if username in user_database:
        return "Username already taken. Please choose a different username."
    else:
        user_database[username] = password
        return "User registered successfully."

def login(username, password):
    """
    Function to handle user login
    """
    if username in user_database:
        if user_database[username] == password:
            return "Login successful."
        else:
            return "Incorrect password."
    else:
        return "User not found. Please register first."

# testing
print(register_user("user1", "pass1")) # "User registered successfully."
print(login("user1", "pass1")) # "Login successful."
print(login("user2", "pass2")) # "User not found. Please register first."
