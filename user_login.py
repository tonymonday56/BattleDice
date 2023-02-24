#user_login.py
# user database to store registered users
import sqlite3
class Users:
    user_database = {'tmonday56': 'savannah1'}
    #def __init__(self):
        # self.user_type_inquiry()
        
    def user_type_inquiry(self):
        user_type = input("Please enter L to Login or R to register: ")
        if user_type.upper() == "L":
            self.login_user()
        elif user_type.upper() == "R":
            self.register_user()
        else:
            print("Error")
            self.user_type_inquiry()
    
        
    def register_user(self):
        """User registration module."""
        username =  input("Please enter username to register: ")
        password =   input("Please enter password to register: ")
   
        if username in self.user_database.keys():
            print("Username already taken. Please choose a different username.")
            self.register_user()
            return "Username already taken. Please choose a different username."
        else:
            self.user_database.update(username) = password
            print("User registered successfully.")
            return "User registered successfully."

    def login_user(self):
        """Module to handle user login"""
        username =  input("Please enter username to login: ")
        password =   input("Please enter password to login: ")
   
        if username in self.user_database.keys():
            if self.user_database[username] == password:
                print("Login successful")
                return "Login successful."
            else:
                print("Error: Incorrect Password.")
                return "Incorrect password."
        else:
            print("Error: User not found. Please register first.")
            return "User not found. Please register first."

# testing

users = Users()
print(users.user_type_inquiry())
#print(register_user("user1", "pass1")) # "User registered successfully."
#print(login("user1", "pass1")) # "Login successful."
#print(login("user2", "pass2")) # "User not found. Please register first."
