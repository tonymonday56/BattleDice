def insertTieDataTable():
        global game_data
        global time_now
        #time_now = time.strftime(t)
        try:
            sqliteConnection = sqlite3.connect("C:\\BattleWar\\dB\\war.sqlite")
            cursor = sqliteConnection.cursor()
            print(Fore.LIGHTGREEN_EX + "Successfully connected to SQLite database [War] for war tie data insertion...")
            print(Style.RESET_ALL)

            
            sqlite_insert_with_param_tie_data = """INSERT INTO tie_data (
                                                                        game_number, 
                                                                        time_now, 
                                                                        hand, 
                                                                        hand_type, 
                                                                        player1_card1, 
                                                                        player1_card2, 
                                                                        player1_card3, 
                                                                        player1_card4, 
                                                                        player2_card1, 
                                                                        player2_card2, 
                                                                        player2_card3, 
                                                                        player2_card4, 
                                                                        tie_winner
                                                                        ) 
                                                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple_tie = (
                                play_data.get("game_number"), 
                                time_now, 
                                play_data.get('hand'), 
                                play_data.get('hand_type'), 
                                play_data.get('player1_card1'), 
                                play_data.get('player1_card2'),
                                play_data.get('player1_card3'), 
                                play_data.get('player1_card4'), 
                                play_data.get('player2_card1'), 
                                play_data.get('player2_card2'), 
                                play_data.get('player2_card3'), 
                                play_data.get('player2_card4'), 
                                play_data.get('tie_winner')
                                )

            cursor.execute(sqlite_insert_with_param_tie_data, data_tuple_tie)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print(Fore.RED + "Failure to insert tie hand data into SQLite database [War] table=tie_data...")
            print(Style.RESET_ALL)
            print("Error: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print(Fore.LIGHTGREEN_EX + "The SQLite connection to insert War Hand data SQLite database [War] is closed...")
                print(Style.RESET_ALL)
