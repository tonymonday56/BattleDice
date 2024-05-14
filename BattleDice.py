# File: BattleDice.py
# initialize 5 dice for each player
import random
# import user_login
# import score
import score_test
import sys

import logging
# Setup logger
logger = logging.getLogger("__name__")
logging.basicConfig(filename="C:\\Projects\\BattleDice\\Logs\\BattleDice.log",
                    encoding="utf-8",
                    filemode="a", 
                    format='%(asctime)s %(levelname)s | %(name)s | %(lineno)d | %(funcName)s | %(message)s', 
                    datefmt='%Y.%m.%d %I:%M:%S %p', 
                    level=logging.DEBUG)

# Game play dictionaries.
discard1 = ""
discard2 = ""
discard3 = ""
discard4 = ""
discard5 = ""
game_number = None
hand_number = 1
player_to_roll = "Player1"
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
        player1_ones -> int
        player1_twos -> int
        player1_threes -> int
        player1_fours -> int
        player1_fives -> int
        player1_sixes -> int
        player1_upperTotal -> int
        player1_upperBonus -> int
        player1_3ofaKind -> int
        player1_4ofaKind -> int
        player1_fullHouse -> int
        player1_smallStraight -> int
        player1_largeStraight -> int
        player1_yahtzee -> int
        player1_chance -> int
        player1_lowerTotal -> int
        player1_total -> int


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
        player2_ones -> int
        player2_twos -> int
        player2_threes -> int
        player2_fours -> int
        player2_fives -> int
        player2_sixes -> int
        player2_upperTotal -> int
        player2_upperBonus -> int
        player2_3ofaKind -> int
        player2_4ofaKind -> int
        player2_fullHouse -> int
        player2_smallStraight -> int
        player2_largeStraight -> int
        player2_yahtzee -> int
        player2_chance -> int
        player2_lowerTotal -> int
        player2_total -> int

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
    """
    This function starts a new game. It checks the player's roll number and
    calls the appropriate roll function.
    """
    logger.info("New game started.")

    # Check player1's roll number and call the appropriate roll function
    if player1_roll.get("player1_rollNumber") == 1:
        # Player1 1st roll
        logger.info("Function firstRoll() being called from play()")
        print("Function firstRoll() being called from play()")
        firstRoll()
    elif player1_roll.get("player1_rollNumber") == 2:
        # Player1 2nd roll
        logger.info("Function secondRoll() being called from play()")
        print("Function secondRoll() being called from play()")
        secondRoll()
    elif player1_roll.get("player1_rollNumber") == 3:
        # Player1 final roll
        logger.info("Function lastRoll() being called from play()")
        print("Function lastRoll() being called from play()")
        lastRoll()



def firstRoll():
    """Initial roll of the dice"""
    logger.info("Function firstRoll() called successfully")
    player1_roll["player1_die1"] = random.randint(1,6)
    player1_roll["player1_die2"] = random.randint(1,6)
    player1_roll["player1_die3"] = random.randint(1,6)
    player1_roll["player1_die4"] = random.randint(1,6)
    player1_roll["player1_die5"] = random.randint(1,6)
    print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"))
    print("Roll Number: "  , player1_roll.get("player1_rollNumber"))
    keep1 = input("Would you like to discard any die?: ")
    if keep1.upper() == "N":
        # Player1 choses to keep current roll.  Call score to score the roll.
        player1_roll["player1_rollNumber"] = player1_roll.get("player1_rollNumber") + 1
        print("score_test() being called from roll() - roll1")
        logger.info("Function score_test() being called from roll() - roll1")
        score_test.score_test()
        return player1_roll.get("player1_die1"),player1_roll.get("player1_die2"), player1_roll.get("player1_die3"), player1_roll.get("player1_die4", player1_roll.get("player1_die5"))    
    
    elif keep1.upper() == "Y": 
        # Player1 choses to not keep rent roll.  Calling make_choice()
        # player1_roll["player1_rollNumber"] = player1_roll.get("player1_rollNumber") + 1
        print("make_choice being called from firstRoll() - Roll1")
        logger.info("Function make_choice() being called from firstroll() - roll1")
        make_choice()

def secondRoll():
    print("Function secondRoll() called successfully")
    logger.info("Function secondRoll() called successfully")
    print("Roll Number: ", player1_roll.get("player1_rollNumber"))
    keep2 = input("Would you like to discard any die?: ")
    if keep2.upper() == "N":
        player1_roll["player1_rollNumber"] = player1_roll.get("player1_rollNumber") + 1
        print("score_test() being called from secondRoll() - roll2")
        logger.info("Function score_test() being called from secondRoll() - roll2")
        score_test.score_test()
    elif keep2.upper() == "Y":
        print("make_choice being called from secondRoll() - roll2")
        logger.info("Function make_choice() being called from secondRoll() - roll2")
        make_choice()


def lastRoll():
    print("Function lastRoll() called successfully")
    logger.info("Function lastRoll() called successfully")
    print("Roll Number: ", player1_roll.get("player1_rollNumber"))
    """
    Go to score roll as no more available rolls.
    """
    print("Function score_test being called from lastRoll()")
    logger.info("Function score_test() being called from lastRoll()")
    score_test.score_test


def make_choice():
    """
    Give player opportunity to modify roll.
    """
    global discard1,discard2, discard3, discard4, discard5
    print("make_choice() started")
    logger.info("Function make_choice() started")
    
    if player1_roll.get("player1_rollNumber") == 1:
        # Roll 1 discard options
        print("Function make_choice() called successfully")
        logger.info("Function make_choice() called successfully")
       
        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        okay_to_reroll = [None, None, None, None, None]
        print("Die to be re-rolled")
        if discard1.upper() == "Y":
            print("Die# 1")
            okay_to_reroll[0] = discard1.upper()
            player1_roll["player1_discard_roll1"].insert(0, "Die#1")
        elif discard1.upper() == "N":
            player1_roll["player1_discard_roll1"].insert(0, "No Change") 
        if discard2.upper() == "Y":
            print("Die# 2")
            okay_to_reroll[1] = discard2.upper()
            player1_roll["player1_discard_roll1"].insert(1, "Die#2")
        elif discard2.upper() == "N":
            player1_roll["player1_discard_roll1"].insert(1, "No Change") 
        if discard3.upper() == "Y":
            print("Die# 3")
            okay_to_reroll[2] = discard3.upper()
            player1_roll["player1_discard_roll1"].insert(2, "Die#3")
        elif discard3.upper() == "N":
            player1_roll["player1_discard_roll1"].insert(2, "No Change") 
        if discard4.upper() == "Y":
            print("Die# 4")
            okay_to_reroll[3]  = discard4.upper()
            player1_roll["player1_discard_roll1"].insert(3, "Die#4")
        elif discard4.upper() == "N":
            player1_roll["player1_discard_roll1"].insert(3, "No Change") 
        if discard5.upper() == "Y":
            print("Die# 5")
            okay_to_reroll[4] = discard5.upper()
            player1_roll["player1_discard_roll1"].insert(4, "Die#5")
        elif discard5.upper() == "N":
            player1_roll["player1_discard_roll1"].insert(4, "No Change") 
        #player1_discard_roll1 = player1_roll.get("player1_discard_roll1")
        print("Roll1 Discards: ", player1_roll.get("player1_discard_roll1"))
        logger.info("Roll1 Discards: ")
        print("Please enter either [Y] or [N] to proceed.  To exit enter CTRL-Z: ")
        save_choice1 = input("Are you satisfied with you discards? [Y] or [N]: ")
        if save_choice1.upper() == "Y":
            # Player1 satisfied with discards.  Calling score()
            #TODO reset player1_roll["player1_rollNumber"] after scoring.
            print("Function score() called successfully")
            logger.info("Function score() called successfully")
            player1_roll["player1_rollNumber"] = player1_roll.get("player1_rollNumber") + 1
            print("Function complete_reroll() called from make_choice()")
            logger.info("Function complete_reroll() called from make_choice()")
            complete_reroll()
        elif save_choice1.upper() == "N":
            # Player1 notsatisfied with discards.  Calling make_choice()
            print("Function make_choice() called successfully")
            logger.info("Function make_choice() called successfully")
            make_choice()
        #TODO
        # print("Function make_choice() called successfully")
        # logger.info("Function make_choice() called successfully")
        
        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        okay_to_reroll = [None, None, None, None, None]
        print("Die to be re-rolled")
        if discard1.upper() == "Y":
            # Player wishes to reroll die1
            print("Die# 1")
            okay_to_reroll[0] = discard1.upper()
            player1_roll["player1_discard_roll2"].insert(0, "Die#1")
        elif discard1.upper() == "N":
            player1_roll["player1_discard_roll2"].insert(0, "No Change") 
        if discard2.upper() == "Y":
            # Player wishes to reroll die2
            print("Die# 2")
            okay_to_reroll[1] = discard2.upper()
            player1_roll["player1_discard_roll2"].insert(1, "Die#2")
        elif discard2.upper() == "N":
            player1_roll["player1_discard_roll2"].insert(1, "No Change") 
        if discard3.upper() == "Y":
            # Player wishes to reroll die3
            print("Die# 3")
            okay_to_reroll[2] = discard3.upper()
            player1_roll["player1_discard_roll2"].insert(2, "Die#3")
        elif discard3.upper() == "N":
            player1_roll["player1_discard_roll2"].insert(2, "No Change") 
        if discard4.upper() == "Y":
            # Player wishes to reroll die4
            print("Die# 4")
            okay_to_reroll[3]  = discard4.upper()
            player1_roll["player1_discard_roll2"].insert(3, "Die#4")
        elif discard4.upper() == "N":
            player1_roll["player1_discard_roll2"].insert(3, "No Change") 
        if discard5.upper() == "Y":
            # Player wishes to reroll die5
            print("Die# 5")
            okay_to_reroll[4] = discard5.upper()
            player1_roll["player1_discard_roll2"].insert(4, "Die#5")
        elif discard5.upper() == "N":
            player1_roll["player1_discard_roll2"].insert(4, "No Change") 
        
        #player1_discard_roll1 = player1_roll.get("player1_discard_roll1")
        print("Roll2 Discards: ", player1_roll.get("player1_discard_roll2"))
        logger.info("Roll2 Discards:")
#         choice = input("Please enter either [Y] or [N].  To exit enter CTRL-Z: ")
#         if choice.upper() == "Y":
#             print("Function complete_reroll() called successfully")
#             logger.info("Function complete_reroll() called successfully")
#             complete_reroll()
#         elif choice.upper() == "N":
#             print("Function roll() called successfully")
def complete_reroll():
    """
    The function takes no parameters.

    The function does not return any values.

    The function first checks if the user wants to discard the first die (discard1) by checking if discard1 is equal to "Y" (case-insensitive). If so, it generates a random number between 1 and 6 (inclusive) and assigns it to player1_die1.

    The function then checks if the user wants to discard the second die (discard2) by checking if discard2 is equal to "Y" (case-insensitive). If so, it generates a random number between 1 and 6 (inclusive) and assigns it to player1_die2.

    The function continues this process for the remaining dice (discard3, discard4, and discard5), generating a random number for each die if the user wants to discard it.

    Finally, the function calls the roll() function to initiate the next round of gameplay.

    Note: The global variables discard1, discard2, discard3, discard4, and discard5 are assumed to be defined and accessible from within the function.
    """

    print("Function complete_reroll() called successfully")
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

    if player1_roll.get("player1_rollNumber") == 1:
       # First roll for player1
        
        player1_roll["second_roll_list"] = [player1_roll.get("player1_die1"), player1_roll.get("player1_die2"), player1_roll.get("player1_die3"),  player1_roll.get("player1_die4"), player1_roll.get("player1_die5")]
        print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        logger.info("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        print("Function secondRoll() being called from complete_reroll()")
        logger.info("Function SecondRoll() being called from complete_reroll()")
        player1_roll["player1_rollNumber"] = int(player1_roll.get("player1_rollNumber")) + 1
        secondRoll()
    elif player1_roll.get("player1_rollNumber") == 2:
        # Second roll for player1
        print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        logger.info("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        print("Function lastRoll() being called from complete_reroll()")
        logger.info("Function lastRoll() being called from complete_reroll()")
        player1_roll["player1_rollNumber"] = int(player1_roll.get("player1_rollNumber")) + 1

        lastRoll()
    elif player1_roll.get("player1_rollNumber") == 3:
        # Last roll for player1
        print("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        logger.info("|", player1_roll.get("player1_die1"), "|", player1_roll.get("player1_die2"), "|", player1_roll.get("player1_die3"), "|",  player1_roll.get("player1_die4"), "|", player1_roll.get("player1_die5"), "|")
        print("Function score_test() being called from complete_reroll()")
        logger.info("Function score_test() being called from complete_reroll()")
        score_test.score_test()
        


if __name__ == "__main__":
    play()