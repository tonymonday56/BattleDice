# Not part of the project.  from Battlewar. add to git ignore.
import time
import sqlite3
from Colorama import Fore, Style
import BattleDice
def insertRollDataTable():
        global game_data
        global time_now
        t = time.now()
        time_now = time.strftime(t)
        try:
            sqliteConnection = sqlite3.connect("C:\\Projects\\BattleDice\\db\\BattleDice.db")
            cursor = sqliteConnection.cursor()
            print(Fore.LIGHTGREEN_EX + "Successfully connected to SQLite database [BattleDice.db] ")
            print(Style.RESET_ALL)

            
            sqlite_insert_with_param_roll_data = """INSERT INTO roll_data (
                                                                        time_now,
                                                                        'player1_name': "",
                                                                        'player1_die1': 0,
                                                                        'player1_die2': 0,
                                                                        'player1_die3': 0,
                                                                        'player1_die4': 0,
                                                                        'player1_die5': 0,
                                                                        'player1_rollNumber': 1,
                                                                        ) 
                                                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple_roll = (
                                time_now, 
                                BattleDice.player1_roll.get('player1_name'), 
                                BattleDice.player1_roll.get('player1_die1'),
                                BattleDice.player1_roll.get('player1_die2'),
                                BattleDice.player1_roll.get('player1_die3'),
                                BattleDice.player1_roll.get('player1_Die4'),
                                BattleDice.player1_roll.get('player1_Die5'),
                                BattleDice.player1_roll.get('player1_rollNumber')
                                )

            cursor.execute(sqlite_insert_with_param_roll_data, data_tuple_roll)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print(Fore.RED + "Failure to insert tie hand data into SQLite database [BattleDice] table=roll_data...")
            print(Style.RESET_ALL)
            print("Error: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print(Fore.LIGHTGREEN_EX + "The SQLite connection to insert BattleDice roll data SQLite database [BattleDice] is closed...")
                print(Style.RESET_ALL)
