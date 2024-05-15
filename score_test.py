# c:/Projects/BattleDice/score_test.py
# File created to test BattleDice functionality
# import BattleDice  as bd
# def score_test(): #    score_test
#     print("Function score_test() called successfully")
#     # logger.info("Function score_test() called successfully")
#     bd.player1_roll["player1_rollNumber"] = 1
#     if bd.pllayer_to_roll == "Player1":
#         print("Player 1 roll completed")
#         bd.player_to_roll = "Player2"
#         print("Player2 roll in progress")
#     elif bd.player_to_roll == "Player2":
#         print("Player 2 roll completed")
#         bd.player_to_roll = "Player1"
#         print("Player1 roll in progress")
#     bd.player_to_roll = "Player2"

p1_scorecard = {
                "p1_ones": 0,
                "p1_twos": 0,
                "p1_threes": 0,
                "p1_fours": 0,
                "p1_fives": 0,
                "p1_sixes": 0,
                "p1_upperTotal": 0,
                "p1_upperBonus": 0,
                "p1_upperTotal": 0,
                "p1_3ofaKind": 0,
                "p1_4ofaKind": 0,
                "p1_fullHouse": 0,
                "p1_smallStraight": 0,
                "p1_largeStraight": 0,
                "p1_bunkerBuster": 0,
                "p1_chance": 0,
                "p1_lowerTotal": 0,
                "p1_total": 0
                }
def print_p1_scorecard():
    """
    Print the scorecard for player 1.

    This function prints out the scores for each category on the scorecard
    for player 1.

    Args:
        p1_ones -> int
        p1_twos -> int
        p1_threes -> int
        p1_fours -> int
        p1_fives -> int
        p1_sixes -> int
        p1_upperTotal -> int
        p1_upperBonus -> int
        p1_3ofaKind -> int
        p1_4ofaKind -> int
        p1_fullHouse -> int
        p1_smallStraight -> int
        p1_largeStraight -> int
        p1_bunkerBuster -> int
        p1_chance -> int
        p1_lowerTotal -> int
        p1_total -> int


    Returns:
        None
    """
    
    print("Ones: ", p1_scorecard.get("p1_ones")) #p1_ones
    print("Twos: ", p1_scorecard.get("p1_twos")) #p1_twos
    print("Threes :", p1_scorecard.get("p1_threes")) #p1_threes
    print("Fours: ", p1_scorecard.get("p1_fours")) #p1_fours
    print("Fives: ", p1_scorecard.get("p1_fives")) #p1_fives
    print("Sixes: ", p1_scorecard.get("p1_sixes")) #p1_sixes
    print("Upper Total: ", p1_scorecard.get("p1_upperAmount")) #p1_upperAmount
    print("Upper Bonus:", p1_scorecard.get("p1_upperBonus")) #p1_upperBonus
    print("Upper Total: ", p1_scorecard.get("p1_upperTotal")) #p1_upperTotal
    print("3 of a Kind: ", p1_scorecard.get("p1_3ofaKind")) #p1_3ofaKind
    print("4 of a Kind: ", p1_scorecard.get("p1_4ofaKind")) #p1_4ofaKind
    print("Full House: ", p1_scorecard.get("p1_fullHouse")) #p1_fullHouse
    print("Small Straight: ", p1_scorecard.get("p1_smallStraight")) #p1_smallStraight
    print("Large Straight: ", p1_scorecard.get("p1_largeStraight")) #p1_largeStraight
    print("Bunker Buster: ", p1_scorecard.get("player1bunkerBuster")) #p1_bunkerBuster
    print("Chance: ", p1_scorecard.get("p1_chance")) #p1_chance
    print("Lower Total: ", p1_scorecard.get("p1_lowerTotal")) #p1_lowerTotal
    print("Total: ", p1_scorecard.get("p1_total")) #p1_total
    #logger.info("Function print_p1_scorecard() completed successfully")

print(print_p1_scorecard())