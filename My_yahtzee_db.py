# my_yahtzee_db.py
#from birdseye import eye
from colorama import Fore, Back, Style
import sqlite3
from sqlite3 import Error
import datetime



def insert_login_data(username):
    '''Insert player turn data. Action to be completed upon turn completion.'''
        #global game_data
       # global time_now
    time_now = datetime.datetime()
    try:
        sqliteConnection = sqlite3.connect("/home/tonymonday56/GitHub/My_yahtzee/db/my_yahtzee.db")
        cursor = sqliteConnection.cursor()
        print(Fore.LIGHTGREEN_EX + "Successfully connected to SQLite database [My_yahtzee]")
        print(Style.RESET_ALL)
        sqlite_insert_user_logins = """INSERT INTO user_logins (
                                                                    username, 
                                                                    time_now) 
                                                                    VALUES
                                                                    (?, ?);"""

        data_tuple_time = (
                            username,
                            time_now,
                            )

        cursor.execute(sqlite_insert_user_logins, data_tuple_tie)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print(Fore.RED + "Failure to insert user login into SQLite database [ My_yahtzee] table=tie_data...")
        print(Style.RESET_ALL)
        print("Error: ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print(Fore.LIGHTGREEN_EX + "The SQLite connection to insert User Login data SQLite database [My_Yahtzee] is closed...")
            print(Style.RESET_ALL)


def insert_game_data(self):
    '''Insert score card data.'''
    pass
    
def insert_registration_data(self):
    '''Insert new player registration data.'''
    pass
    
#my_db = My_db()
#my_db.insert_game_data()