#player2_wins_game.py
import time

def player2_wins_game():
    time.sleep(1)
    print("Player 2 Wins Game!")
    time.sleep(1)

    with open("C:\\Projects\\BattleWar2\\dB\\log\\wargames.dat", "a") as f:
        f.write("Player2 Wins Game!\n")
        f.write("----------------------------------------------\n")

    with open("C:\\Projects\\BattleWar2\\dB\\log\\warplayer2wins.dat", "r") as f:
        player2wins = int(f.readline())

    with open("C:\\Projects\\BattleWar2\\dB\\log\\warplayer2wins.dat", "w") as f:
        f.write(str(player2wins + 1))

    playData['game_winner'] = "Player 2"
    playData['game_winner_name'] = playData.get('player2_username')
    playData['game_loser'] = "Player 1"
    playData['game_loser_name'] = playData.get('player1_username')

    print("play_winner_name: ", playData.get('game_winner_name'))
    print("game_winner: ", playData.get('game_winner'))
    print("game_loser_name: ", playData.get('game_loser_name'))
    print("game_loser: ", playData.get('game_loser_name'))

    print(Fore.BLUE + '.......................................insertUserInfo() called from player2_wins_game()...')
    insert_user_info()
    print("printPlayData() called from player2winsgame()")
    printPlayData()