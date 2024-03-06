#user_login.py
# user database to store registered users
from time import sleep
from BattleDiceDB import BattleDice_db
import sqlite3
import logging
logging.basicConfig(filename='C:\\Projects\\BattleDice\\Logs\\example.log', encoding='utf-8', level=logging.DEBUG)
global user_database
user_database = {'tmonday56': 'Savannah1'}
import logger
logging.basicConfig(filename='C:\\Projects\\BattleDice\\Logs\\BattleDice.log', encoding='utf-8', level=logging.DEBUG)

class Users:
    #    user_database = {'tmonday56': 'savannah1'}
    #def __init__(self):
    # self.user_type_inquiry()
    def user_type_inquiry(self):
        """Module to handle user type inquiry."""
        # Determine if it is a new or returning user.
        logger.info("user_type_inquiry() starting...")
        user_type = input("Please enter L to Login or R to register: ")
        if user_type.upper() == "L":
            # Indicates returning user.
            logger.info("Return user: ", "Input L for user_type_inquiry")
            logger.info("user_type_inquiry() exiting...")
            logger.info("login_user() called by user_type_inquiry()")
            self.login_user()
        elif user_type.upper() == "R":
            # Indicates new user.
            logger.info("New user: ", "Input R [Register User]for user_type_inquiry")
            logger.info("user_type_inquiry() exiting...")
            logger.info("register_user() called by user_type_inquiry()")
            self.register_user()
        else:
            # user did not enter L or R
            print("Error")
            print("Please enter L to Login or R to register.")
            logger.info("Error: ", "Input other than L or R for user_type_inquiry")
            logger.info("user_type_inquiry() calling user_type_inquiry(): Restarting login process over again.")
            self.user_type_inquiry()
    
        
    def register_user(self):
        """User registration module."""
        logger.info("register_user() starting...")
        global user_database
        username =  input("Please enter username to register: ")
        user_password =   input("Please enter password to register: ")
   
        if username in user_database.keys():
            print("Username already taken. Please choose a different username.")
            self.register_user()
            return "Username already taken. Please choose a different username."
        else:
            user_database['username'] = user_password
            logger.info("register_user() exiting...")
            print("User registered successfully.")
            return "User registered successfully."

    def login_user(self):
        """Module to handle user login"""
        logger.info("login_user() starting...")
        global user_database
        username =  input("Please enter username to login: ")
        user_password =   input("Please enter password to login: ")
   
        if username in user_database.keys():
            if user_database[username] == user_password:
                
                BattleDice_db.insert_login_data(username)
                logger.info("login_user() exiting...")

                print("Login successful")
                sleep(1)
                return "Login successful."
            else:
                print("Error: Incorrect Password.")
                sleep(1)
                logger.info("login_user() calling login_user...")
                return "Incorrect password."

        else:
            print("Error: User not found. Please register first.")
            sleep(1)
            logger.info("login_user() calling register_user...")
            self.register_user()
            return "User not found. Please register first."

# testing

users = Users()
print(users.user_type_inquiry())
#print(register_user("user1", "pass1")) # "User registered successfully."
#print(login("user1", "pass1")) # "Login successful."
#print(login("user2", "pass2")) # "User not found. Please register first."
