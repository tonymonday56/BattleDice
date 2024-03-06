# File: BattleDice.py
# initialize 5 dice for each player
import random
# import user_login
# import score
import score_test
import sys
import logging
# Setup logger
logging.basicConfig(filename="C:\\Projects\\BattleDice\\Logs\\BattleDice.log",
                    encoding="utf-8",
                    filemode="a", 
                    format='%(asctime)s %(levelname)s | %(name)s | %(lineno)d | %(funcName)s | %(message)s', 
                    datefmt='%Y.%m.%d %I:%M:%S %p', 
                    level=logging.DEBUG)
logger = logging.getLogger("__name__")
# Game play dictionaries.
player1_roll = {
            "player1_name": "",
            "player1_die1": 0,
            "player1_die2": 0,
            "player1_die3": 0,
            "player1_die4": 0,
            "player1_die5": 0,
            "player1_rollNumber": 1,
            "player1_firstRollList": [],
            "player1_discard_roll1": [],
            "player1_secondRollList": [],
            "player1_discard_roll2": [],
            "player1_thirdRollList": []
            }

# player1 scorecard
player1_scorecard = {
                "player1_ones": 0,
                "player1_twos": 0,
                "player1_threes": 0,
                "player1_fours": 0,
                "player1_fives": 0,
                "player1_sixes": 0,
                "player1_upperTotal": 0,
                "player1_upperBonus": 0,
                "player1_upperTotal": 0,
                "player1_3ofaKind": 0,
                "player1_4ofaKind": 0,
                "player1_fullHouse": 0,
                "player1_smallStraight": 0,
                "player1_largeStraight": 0,
                "player1_yahtzee": 0,
                "player1_chance": 0,
                "player1_lowerTotal": 0,
                "player1_total": 0
                }

# Player2 roll
player2_roll = {
                "player2_name": "",
                "player2_die1": 0,
                "player2_die2": 0,
                "player2_die3": 0,
                "player2_die4": 0,
                "player2_die5": 0,
                "player2_rollNumber": 1,
                "player2_firstRollList": [],
                "player2_discard_roll1": [],
                "player2_secondRollList": [],
                "player2_discard_roll2": [],
                "player2_thirdRollList": []
                }

# player2_scorecard
player2_scorecard  = {
               "player2_ones": 0,
                "player2_twos": 0,
                "player2_threes": 0,
                "player2_fours": 0,
                "player2_fives": 0,
                "player2_sixes": 0,
                "player2_upperTotal": 0,
                "player2_upperBonus": 0,
                "player2_upperTotal": 0,
                "player2_3ofaKind": 0,
                "player2_4ofaKind": 0,
                "player2_fullHouse": 0,
                "player2_smallStraight": 0,
                "player2_largeStraight": 0,
                "player2_yahtzee": 0,
                "player2_chance": 0,
                "player2_lowerTotal": 0,
                "player2_total": 0
                }

def print_player1_scorecard():
    """
    Print the scorecard for player 1.

    This function prints out the scores for each category on the scorecard
    for player 1.

    Args:
        None

    Returns:
        None
    """
    
    print("Ones: ", player1_scorecard.get("player1_ones")) #player1_ones
    print("Twos: ", player1_scorecard.get("player1_twos")) #player1_twos
    print("Threes :", player1_scorecard.get("player1_threes")) #player1_threes
    print("Fours: ", player1_scorecard.get("player1_fours")) #player1_fours
    print("Fives: ", player1_scorecard.get("player1_fives")) #player1_fives
    print("Sixes: ", player1_scorecard.get("player1_sixes")) #player1_sixes
    print("Upper Total: ", player1_scorecard.get("player1_upperAmount")) #player1_upperAmount
    print("Upper Bonus:", player1_scorecard.get("player1_upperBonus")) #player1_upperBonus
    print("Upper Total: ", player1_scorecard.get("player1_upperTotal")) #player1_upperTotal
    print("3 of a Kind: ", player1_scorecard.get("player1_3ofaKind")) #player1_3ofaKind
    print("4 of a Kind: ", player1_scorecard.get("player1_4ofaKind")) #player1_4ofaKind
    print("Full House: ", player1_scorecard.get("player1_fullHouse")) #player1_fullHouse
    print("Small Straight: ", player1_scorecard.get("player1_smallStraight")) #player1_smallStraight
    print("Large Straight: ", player1_scorecard.get("player1_largeStraight")) #player1_largeStraight
    print("Yahtzee: ", player1_scorecard.get("player1_yahtzee")) #player1_yahtzee
    print("Chance: ", player1_scorecard.get("player1_chance")) #player1_chance
    print("Lower Total: ", player1_scorecard.get("player1_lowerTotal")) #player1_lowerTotal
    print("Total: ", player1_scorecard.get("player1_total")) #player1_total
    logger.info("Function print_player1_scorecard() completed successfully")
def print_player2_scorecard():
    """
    Print the scorecard for player 2.

    This function prints out the scores for each category on the scorecard
    for player 2.

    Args:
        None

    Returns:
        None
    """
    print("Ones: ", player2_scorecard.get("player2_ones")) #player2_ones
    print("Twos: ", player2_scorecard.get("player2_twos")) #player2_twos
    print("Threes :", player2_scorecard.get("player2_threes")) #player2_threes
    print("Fours: ", player2_scorecard.get("player2_fours")) #player2_fours
    print("Fives: ", player2_scorecard.get("player2_fives")) #player2_fives
    print("Sixes: ", player2_scorecard.get("player2_sixes")) #player2_sixes
    print("Upper Total: ", player2_scorecard.get("player2_upperAmount")) #player2_upperAmount
    print("Upper Bonus:", player2_scorecard.get("player2_upperBonus")) #player2_upperBonus
    print("Upper Total: ", player2_scorecard.get("player2_upperTotal")) #player2_upperTotal
    print("3 of a Kind: ", player2_scorecard.get("player2_3ofaKind")) #player2_3ofaKind
    print("4 of a Kind: ", player2_scorecard.get("player2_4ofaKind")) #player2_4ofaKind
    print("Full House: ", player2_scorecard.get("player2_fullHouse")) #player2_fullHouse
    print("Small Straight: ", player2_scorecard.get("player2_smallStraight")) #player2_smallStraight
    print("Large Straight: ", player2_scorecard.get("player2_largeStraight")) #player2_largeStraight
    print("Yahtzee: ", player2_scorecard.get("player2_yahtzee")) #player2_yahtzee
    print("Chance: ", player2_scorecard.get("player2_chance")) #player2_chance
    print("Lower Total: ", player2_scorecard.get("player2_lowerTotal")) #player2_lowerTotal
    print("Total: ", player2_scorecard.get("player2_total")) #player2_total
    logger.info("Function print_player2_scorecard() completed successfully")


def play():
    if player1_roll.get("player1_rollNumber") == 1: # player
        logger.info("New game started.")
        firstRoll()
        logger.info("Function frirstroll() being called from play()")
        #score_test.score_test()
    elif player1_roll.get("player1_roll.player1_rollNumber") == 2:
        secondRoll()
        logger.info("Function secondRoll() being called from play()")
    elif player1_roll.get("player1_roll.player1_rollNumber") == 3:
        lastRoll()
        logger.info("Function lastRoll() being called from play()")
    
        # elif player1_card["Twos"] = 0
        #     player1_card["Threes"] = 0
        #     player1_card["Fours"] = 0
        #     player1_card["Fives"] = 0
        #     player1_card["Sixes"] = 0

def firstRoll():
    logger.info("Function roll() called successfully")
    """Initial roll of the dice"""
    player1_roll["player1_die1"] = random.randint(1,6)
    player1_roll["player1_die2"] = random.randint(1,6)
    player1_roll["player1_die3"] = random.randint(1,6)
    player1_roll["player1_die4"] = random.randint(1,6)
    player1_roll["player1_die5"] = random.randint(1,6)
    print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"))
    print()
    keep1 = input("Would you like to discard any die?: ")
    if keep1.upper() == "N":
        #score()
        return player1_roll.get("player1_die1"), player1_roll.get("player1_die2"), player1_roll.get("player1_die3"), player1_roll.get("player1_die4", player1_roll.get("player1_die5"))
    elif keep1.upper() == "Y":
        print("make_choice being called from roll() - roll1")
        logger.info("Function make_choice() being called from roll() - roll1")
        make_choice()

def secondRoll():
    logger.info("Function secondRoll() called successfully")
    keep2 = input("Would you like to discard any die?: ")
    if keep2.upper() == "N":
        score_test.score_test()
    elif keep2.upper() == "Y":
        print("make_choice being called from secondRoll() - roll2")
        logger.info("Function make_choice() being called from secondRoll() - roll2")
        make_choice()


def lastRoll():
    """
    Go to score roll as no more available rolls.
    """
    score_test.score_test()

discard2 = ""
discard3 = ""
discard4 = ""
discard5 = ""

def make_choice():
    """
    Give player opportunity to modify roll.
    """

    logger.info("Function make_choice() called successfully")
    global discard1,discard2, discard3, discard4, discard5
    discard1 = input("Would you like to discard die1? Y for Yes:")
    discard2 = input("Would you like to discard die2? Y for Yes:")
    discard3 = input("Would you like to discard die3? Y for Yes:")
    discard4 = input("Would you like to discard die4? Y for Yes:")
    discard5 = input("Would you like to discard die5? Y for Yes:")
    okay_to_reroll = [None, None, None, None, None]
    if discard1.upper() == "Y":
        print("Die# 1")
        okay_to_reroll[0] = discard1.upper()
    if discard2.upper() == "Y":
        print("Die# 2")
        okay_to_reroll[1] = discard2.upper()
    if discard3.upper() == "Y":
        print("Die# 3")
        okay_to_reroll[2] = discard3.upper()
    if discard4.upper() == "Y":
        print("Die# 4")
        okay_to_reroll[3]  = discard4.upper()
    if discard5.upper() == "Y":
        print("Die# 5")
        okay_to_reroll[4] = discard5.upper()
       # put in confirmation if == "N" go back to choice
    print("You okay with reroll status?")
    reroll_check = input("Enter [Y] to continue with reroll or [N] to re-select the die: ")
    if reroll_check.upper() == "Y":
        complete_reroll()
    elif reroll_check.upper() ==  "N":
        make_choice()
    else:
        print("Please enter either [Y] or [N].  To exit enter CTRL-Z: ")
        make_choice()
            
def complete_reroll():
    """
    Completes a reroll of the dice based on the user"s input for discarding dice.

    The function takes no parameters.

    The function does not return any values.

    The function first checks if the user wants to discard the first die (discard1) by checking if discard1 is equal to "Y" (case-insensitive). If so, it generates a random number between 1 and 6 (inclusive) and assigns it to player1_die1.

    The function then checks if the user wants to discard the second die (discard2) by checking if discard2 is equal to "Y" (case-insensitive). If so, it generates a random number between 1 and 6 (inclusive) and assigns it to player1_die2.

    The function continues this process for the remaining dice (discard3, discard4, and discard5), generating a random number for each die if the user wants to discard it.

    Finally, the function calls the roll() function to initiate the next round of gameplay.

    Note: The global variables discard1, discard2, discard3, discard4, and discard5 are assumed to be defined and accessible from within the function.
    """
    logger.info("Function complete_reroll() called successfully")

    global discard1, discard2, discard3, discard4, discard5
    if discard1.upper() == "Y":
        player1_roll["player_die1"] = random.randint(1,6)
    if discard2.upper() == "Y":
        player1_roll["player1_die2"] = random.randint(1,6)
    if discard3.upper() == "Y":
        player1_roll["player1_die3"] = random.randint(1,6)
    if discard4.upper() == "Y":
        player1_roll["player1_die4"] = random.randint(1,6)
    if discard5.upper() == "Y":
        player1_roll["player1_die5"] = random.randint(1,6)
    logger.info("Function roll() called from complete_reroll()")
    if player1_roll.get("player1_rollNumber") == 1 or player1_roll.get("player1_rollNumber") == 2:
        player1_roll["player1_rollNumber"] = int(player1_roll.get("player1_rollNumber")) + 1
        print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        logger.info("Function roll() being called from complete_reroll()")
        secondRoll()
    if player1_roll.get("player1_rollNumber") == 3:
        # player1_roll["player1_rollNumber"] = int(player1_roll.get("player1_rollNumber")) + 1
        print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        logger.info("Function score() being called from complete_reroll()")
        lastRoll()
        


if __name__ == "__main__":
    play()