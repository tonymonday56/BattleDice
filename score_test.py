# c:/Projects/BattleDice/score_test.py
# File created to test BattleDice functionality
import BattleDice  as bd
def score_test(): #    score_test
    print("Function score_test() called successfully")
    # logger.info("Function score_test() called successfully")
    bd.player1_roll["player1_rollNumber"] = 1
    if bd.pllayer_to_roll == "Player1":
        print("Player 1 roll completed")
        bd.player_to_roll = "Player2"
        print("Player2 roll in progress")
    elif bd.player_to_roll == "Player2":
        print("Player 2 roll completed")
        bd.player_to_roll = "Player1"
        print("Player1 roll in progress")
    bd.player_to_roll = "Player2"