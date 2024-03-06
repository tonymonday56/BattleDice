# BattleDiceDB.py
from colorama import Fore, Back, Style
import sqlite3
from sqlite3 import Error
import time
import logging
logging.basicConfig(filename='C:\\Projects\\BattleWar2\\Logs\\BattleDice.log', format='%(levelname)s | %(asctime)s | %(lineno)d | %(funcName)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.INFO)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

class BattleDice_db:
    def insert_login_data(self, username):
        '''Insert player login data.'''
        t = time.asctime()
        time_now = time.strftime(t)
        try:
            sqliteConnection = sqlite3.connect("C:\Projects\BattleDice\db\BattleDice.db")
            cursor = sqliteConnection.cursor()
            print(Fore.LIGHTGREEN_EX + "class=BattleDice_db module=insert_login_data")
            print(Fore.LIGHTGREEN_EX + "Successfully connected to SQLite database [BattleDice.db]")
            print(Style.RESET_ALL)
            logging.info("class=BattleDice_db module=insert_login_data")
            logging.info("Successfully connected to SQLite database [BattleDice.db]")
            
            
            sqlite_insert_user_logins = """INSERT INTO user_logins (
                                                                        username, 
                                                                        login_time) 
                                                                        VALUES
                                                                        (?, ?);"""

            data_tuple_time = (
                                username,
                                time_now,
                                )

            cursor.execute(sqlite_insert_user_logins, data_tuple_time)
            sqliteConnection.commit()
            print(Fore.LIGHTGREEN_EX + "class=BattleDice_db module=insert_login_data")
            print(Fore.LIGHTGREEN_EX + "User login data successfully inserted into user_logins table of BattleDice_db")
            logging.info("class=BattleDice_db module=insert_login_data")
            logging.info("User login data successfully inserted into user_logins table of BattleDice_db")
            print(Style.RESET_ALL)
            cursor.close()

        except sqlite3.Error as error:
            print(Fore.RED + "Error: ", error)
            print(Fore.RED + "class=BattleDice_db module=insert_login_data")
            print(Fore.RED + "Failure to insert user login into SQLite database [BattleDice] table=user_logins...")
            logging.warning("Failure to insert user login into SQLite database [BattleDice] table=user_logins...")
            logging.warning("Failure to insert user login into SQLite database [BattleDice] table=user_logins...")
            
            print(Style.RESET_ALL)
            
            
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                logging.info("class=BattleDice_db module=insert_login_data")
                logging.info("The SQLite connection to insert User Login data SQLite database [BattleDice] is closed...")
                print(Fore.LIGHTGREEN_EX + "class=BattleDice_db module=insert_login_data")
                print(Fore.LIGHTGREEN_EX + "The SQLite connection to insert User Login data SQLite database [BattleDice] is closed...")
                print(Style.RESET_ALL)

    
    def insert_game_data(self):
        '''Insert score card data.'''
        pass
        
    def insert_registration_data(self):
        '''Insert new player registration data.'''
        pass
    
battleDice_db = BattleDice_db()
battleDice_db.insert_login_data('tonymonday56')