# File: BattleDice.py
# initialize 5 dice for each player
import random
# import user_login
import sys
from time import sleep
import logging
# Setup logger
logger = logging.getLogger("bd_logger")
logging.basicConfig(filename="C:\\Projects\\BattleDice\\Logs\\BattleDice.log",
                    encoding="utf-8",
                    filemode="a", 
                    format='%(asctime)s | %(levelname)s | %(name)s | %(lineno)d | %(funcName)s | %(message)s', 
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
roll_number = 1
p1_roll = {
            "p1_name": "",
            "p1_die1": 0,
            "p1_die2": 0,
            "p1_die3": 0,
            "p1_die4": 0,
            "p1_die5": 0,
            "p1_firstRollList": [],
            "p1_discard_roll1": [],
            "p1_secondRollList": [],
            "p1_discard_roll2": [],
            "p1_thirdRollList": []
            }


# Player2 roll
p2_roll = {
                "p2_name": "",
                "p2_die1": 0,
                "p2_die2": 0,
                "p2_die3": 0,
                "p2_die4": 0,
                "p2_die5": 0,
                "p2_firstRollList": [],
                "p2_discard_roll1": [],
                "p2_secondRollList": [],
                "p2_discard_roll2": [],
                "p2_thirdRollList": []
                }


def reset_roll():
    """Reset roll data."""
    global roll_number
    global p1_roll
    global p2_roll
    global discard1, discard2, discard3, discard4, discard5
    discard1, discard2, discard3, discard4, discard5 = "", "", "", "", ""
    roll_number = 1
    p1_roll["p1_die1"] = 0
    p1_roll["p1_die2"] = 0
    p1_roll["p1_die3"] = 0
    p1_roll["p1_die4"] = 0
    p1_roll["p1_die5"] = 0
    p1_roll["p1_firstRollList"] = []
    p1_roll["p1_discard_roll1"] = []
    p1_roll["p1_secondRollList"] = []
    p1_roll["p1_discard_roll2"] = []
    p1_roll["p1_thirdRollList"] = []
    p2_roll["p2_die1"] = 0
    p2_roll["p2_die2"] = 0
    p2_roll["p2_die3"] = 0
    p2_roll["p2_die4"] = 0
    p2_roll["p2_die5"] = 0
    p2_roll["p2_firstRollList"] = []
    p2_roll["p2_discard_roll1"] = []
    p2_roll["p2_secondRollList"] = []
    p2_roll["p2_discard_roll2"] = []
    p2_roll["p2_thirdRollList"] = []


def play():
    """The first phase of a new game. Checks the player's roll number and
    calls the appropriate roll function."""
    logger.info("New game started.")
    print("Function reset_roll() called from play()")
    reset_roll()

    # Check player1's roll number and call the appropriate roll function
    if roll_number == 1:
        # Player1 1st roll
        logger.info("Function firstRoll() being called from play()")
        print("Function firstRoll() being called from play()")
        firstRoll()
    elif roll_number == 2:
        # Player1 2nd roll
        logger.info("Function secondRoll() being called from play()")
        print("Function secondRoll() being called from play()")
        secondRoll()
    elif roll_number == 3:
        # Player1 final roll
        logger.info("Function lastRoll() being called from play()")
        print("Function lastRoll() being called from play()")
        lastRoll()


def firstRoll():
    """First of 3 possible rolls for players turn."""
    global roll_number
    import bd_score
    """Initial roll of the dice"""
    logger.info("Function firstRoll() called successfully")
    p1_roll["p1_die1"] = random.randint(1, 6)
    p1_roll["p1_die2"] = random.randint(1, 6)
    p1_roll["p1_die3"] = random.randint(1, 6)
    p1_roll["p1_die4"] = random.randint(1, 6)
    p1_roll["p1_die5"] = random.randint(1, 6)
    p1_firstRollList = [p1_roll.get("p1_die1"),
                        p1_roll.get("p1_die2"),
                        p1_roll.get("p1_die3"),
                        p1_roll.get("p1_die4"),
                        p1_roll.get("p1_die5")]
    print("|", p1_roll.get("p1_die1"),
          "|", p1_roll.get("p1_die2"),
          "|", p1_roll.get("p1_die3"),
          "|", p1_roll.get("p1_die4"),
          "|", p1_roll.get("p1_die5"))
    print("Roll Number: ", roll_number)
    keeper1 = input("Would you like to discard any die?: ")
    if keeper1.upper() == "N":
        # Player1 choses to keeper current roll.  Call score to score the roll.
        roll_number = roll_number + 1
        print("score_test() being called from roll() - roll1")
        logger.info("Function score_test() being called from roll() - roll1")
        keeper1 = ""
        bd_score.battleDice_score(p1_firstRollList)
        print(bd_score.p1_scorecard)
        sleep(10)
        if bd_score.game_status == "In Progress":
            play()
    elif keeper1.upper() == "Y": 
        # Player1 choses to not keeper current roll.  Calling make_choice()
        # p1_roll["p1_rollNumber"] = p1_roll.get("p1_rollNumber") + 1
        print("make_choice being called from firstRoll() - Roll1")
        logger.info("Function make_choice() being called from firstroll() - roll1")
        keeper1 = ""
        make_choice()


def secondRoll():
    """First of 3 possible rolls for players turn."""
    import bd_score
    global roll_number
    print("Function secondRoll() called successfully")
    logger.info("Function secondRoll() called successfully")
    print("Roll Number: ", roll_number)
    print("|", p1_roll.get("p1_die1"),
          "|", p1_roll.get("p1_die2"),
          "|", p1_roll.get("p1_die3"),
          "|", p1_roll.get("p1_die4"),
          "|", p1_roll.get("p1_die5"))
    keeper2 = input("Would you like to discard any die?: ")
    if keeper2.upper() == "N":
        p1_secondRollList = [
                            p1_roll.get("p1_die1"),
                            p1_roll.get("p1_die2"),
                            p1_roll.get("p1_die3"),
                            p1_roll.get("p1_die4"),
                            p1_roll.get("p1_die5")
                            ]
        roll_number = roll_number + 1
        print("score_test() being called from secondRoll() - roll2")
        logger.info("Function score_test() being called from secondRoll()")
        keeper2 = ""
        bd_score.battleDice_score(p1_secondRollList)
        print(bd_score.score_choice("p1_scorecard"))
        sleep(10)
        if bd_score.game_status == "In Progress":
            play()
    elif keeper2.upper() == "Y":
        print("make_choice being called from secondRoll() - roll2")
        logger.info("Function make_choice() being called from secondRoll()")
        keeper2 = ""
        make_choice()


def lastRoll():
    """Players final of 3 possible rolls for players turn."""
    global roll_number
    import bd_score
    p1_lastRollList = [
                        p1_roll.get("p1_die1"),
                        p1_roll.get("p1_die2"),
                        p1_roll.get("p1_die3"),
                        p1_roll.get("p1_die4"),
                        p1_roll.get("p1_die5")
                       ]
    print("Function lastRoll() called successfully")
    logger.info("Function lastRoll() called successfully")
    print("Roll Number: ", roll_number)
    """
    Go to score roll as no more available rolls.
    """
    print("Function score_test being called from lastRoll()")
    logger.info("Function score_test() being called from lastRoll()")
    bd_score.battleDice_score(p1_lastRollList)
    print(bd_score.score_choice("p1_scorecard"))
    sleep(10)
    if bd_score.game_status == "In Progress":
        play()


def make_choice():
    """Give player opportunity to modify roll."""
    print("Function make_choice() called successfully")
    logger.info("Function make_choice() called successfully")
    print("make_choice() started")
    logger.info("Function make_choice() started")
    global roll_number
    global discard1, discard2, discard3, discard4, discard5
    okay_to_reroll = [None, None, None, None, None]
    if roll_number == 1:
        print("|", p1_roll.get("p1_die1"),
                "|", p1_roll.get("p1_die2"),
                "|", p1_roll.get("p1_die3"),
                "|", p1_roll.get("p1_die4"),
                "|", p1_roll.get("p1_die5"))
        # Roll 1 discard options
        discard_all = input ("Would you like to discard all die? A for All:")
        if discard_all.upper() == "A":
            discard1 == "Y"
            discard2 == "Y"
            discard1 == "Y"
            discard2 == "Y"
            discard1 == "Y"
            if discard1.upper() == "Y":
                print("Die# 1")
                okay_to_reroll[0] = discard1.upper()
                p1_roll["p1_discard_roll1"].insert(0, "Die#1")
            elif discard1.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(0, "No Change")
            if discard2.upper() == "Y":
                print("Die# 2")
                okay_to_reroll[1] = discard2.upper()
                p1_roll["p1_discard_roll1"].insert(1, "Die#2")
            elif discard2.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(1, "No Change")
            if discard3.upper() == "Y":
                print("Die# 3")
                okay_to_reroll[2] = discard3.upper()
                p1_roll["p1_discard_roll1"].insert(2, "Die#3")
            elif discard3.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(2, "No Change")
            if discard4.upper() == "Y":
                print("Die# 4")
                okay_to_reroll[3] = discard4.upper()
                p1_roll["p1_discard_roll1"].insert(3, "Die#4")
            elif discard4.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(3, "No Change")
            if discard5.upper() == "Y":
                print("Die# 5")
                okay_to_reroll[4] = discard5.upper()
                p1_roll["p1_discard_roll1"].insert(4, "Die#5")
            elif discard5.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(4, "No Change")
            # Player1 p1_roll["p1_discard_roll1"] = p1_roll.get("p1_discard_roll1")
            print("Roll1 Discards: ", p1_roll.get("p1_discard_roll1"))
            logger.info("Roll1 Discards:: %s", p1_roll.get("p1_discard_roll1"))
            print("Please enter either [Y/N] to proceed.  To exit enter CTRL-Z: ")
            save_choice1 = input("Are you satisfied with you discards? [Y/N]: ")
            if save_choice1.upper() == "Y":
                # Player1 satisfied with discards.  Calling score()
                # TODO reset p1_roll["p1_rollNumber"] after scoring.
                # print("Function bd_score() called successfully")
                # logger.info("Function bd_score() called successfully")
                # roll_number = roll_number + 1
                print("Function complete_reroll() called from make_choice()")
                logger.info("Function complete_reroll() called from make_choice()")
                save_choice1 = ""
                complete_reroll()
            elif save_choice1.upper() == "N":
                # Player1 notsatisfied with discards.  Calling make_choice()
                print("Function make_choice() called successfully")
                logger.info("Function make_choice() called successfully")
                save_choice1 = ""
                make_choice()
        elif roll_number == 2:
        #TODO
            # print("Function make_choice() called successfully")
            # logger.info("Function make_choice() called successfully")
            discard1 = input("Would you like to discard die1? Y for Yes:")
            discard2 = input("Would you like to discard die2? Y for Yes:")
            discard3 = input("Would you like to discard die3? Y for Yes:")
            discard4 = input("Would you like to discard die4? Y for Yes:")
            discard5 = input("Would you like to discard die5? Y for Yes:")
            okay_to_reroll2 = [None, None, None, None, None]
            print("Die to be re-rolled")
            if discard1.upper() == "Y":
                # Player wishes to reroll die1
                print("Die# 1")
                okay_to_reroll2[0] = discard1.upper()
                p1_roll["p1_discard_roll2"].insert(0, "Die#1")
            elif discard1.upper() == "N":
                p1_roll["p1_discard_roll2"].insert(0, "No Change")
            if discard2.upper() == "Y":
                # Player wishes to reroll die2
                print("Die# 2")
                okay_to_reroll2[1] = discard2.upper()
                p1_roll["p1_discard_roll2"].insert(1, "Die#2")
            elif discard2.upper() == "N":
                p1_roll["p1_discard_roll2"].insert(1, "No Change")
            if discard3.upper() == "Y":
                # Player wishes to reroll die3
                print("Die# 3")
                okay_to_reroll[2] = discard3.upper()
                p1_roll["p1_discard_roll2"].insert(2, "Die#3")
            elif discard3.upper() == "N":
                p1_roll["p1_discard_roll2"].insert(2, "No Change")
            if discard4.upper() == "Y":
                # Player wishes to reroll die4
                print("Die# 4")
                okay_to_reroll2[3] = discard4.upper()
                p1_roll["p1_discard_roll2"].insert(3, "Die#4")
            elif discard4.upper() == "N":
                p1_roll["p1_discard_roll2"].insert(3, "No Change")
            if discard5.upper() == "Y":
                # Player wishes to reroll die5
                print("Die# 5")
                okay_to_reroll2[4] = discard5.upper()
                p1_roll["p1_discard_roll2"].insert(4, "Die#5")
            elif discard5.upper() == "N":
                p1_roll["p1_discard_roll2"].insert(4, "No Change")
            # Player1 [p1] discard_roll1 = p1_roll.get("p1_discard_roll1")
            print("Roll2 Discards: ", p1_roll.get("p1_discard_roll2"))
            logger.info("Roll2 Discards:: %s", p1_roll.get("p1_discard_roll2"))
            print("Please enter either [Y/N] to proceed.  To exit enter CTRL-Z: ")
            save_choice2 = input("Are you satisfied with your discards? [Y/N]: ")
            if save_choice2.upper() == "Y":
                # Player1 satisfied with discards.  Calling score()
                # TODO reset p1_roll["p1_rollNumber"] after scoring.
                # print("Function bd_score() called successfully")
                # logger.info("Function bd_score() called successfully")
                # roll_number = roll_number + 1
                print("Function complete_reroll() called from make_choice()")
                logger.info("Function complete_reroll() called from make_choice()")
                save_choice2 = ""
                complete_reroll()
            elif save_choice2.upper() == "N":
                # Player1 notsatisfied with discards.  Calling make_choice()
                print("Function make_choice() called successfully")
                logger.info("Function make_choice() called successfully")
                save_choice2 = ""
                make_choice()
    #         choice = input("Please enter either [Y/N].  To exit enter CTRL-Z: ")
    #         if choice.upper() == "Y":
    #             print("Function complete_reroll() called successfully")
    #             logger.info("Function complete_reroll() called successfully")
    #             complete_reroll()
    #         elif choice.upper() == "N":
    #             print("Function roll() called successfully")
        elif discard_all.upper() == "N":
            discard1 = input("Would you like to discard die1? Y for Yes:")
            discard2 = input("Would you like to discard die2? Y for Yes:")
            discard3 = input("Would you like to discard die3? Y for Yes:")
            discard4 = input("Would you like to discard die4? Y for Yes:")
            discard5 = input("Would you like to discard die5? Y for Yes:")
            if discard1.upper() == "Y":
                print("Die# 1")
                okay_to_reroll[0] = discard1.upper()
                p1_roll["p1_discard_roll1"].insert(0, "Die#1")
            elif discard1.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(0, "No Change")
            if discard2.upper() == "Y":
                print("Die# 2")
                okay_to_reroll[1] = discard2.upper()
                p1_roll["p1_discard_roll1"].insert(1, "Die#2")
            elif discard2.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(1, "No Change")
            if discard3.upper() == "Y":
                print("Die# 3")
                okay_to_reroll[2] = discard3.upper()
                p1_roll["p1_discard_roll1"].insert(2, "Die#3")
            elif discard3.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(2, "No Change")
            if discard4.upper() == "Y":
                print("Die# 4")
                okay_to_reroll[3] = discard4.upper()
                p1_roll["p1_discard_roll1"].insert(3, "Die#4")
            elif discard4.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(3, "No Change")
            if discard5.upper() == "Y":
                print("Die# 5")
                okay_to_reroll[4] = discard5.upper()
                p1_roll["p1_discard_roll1"].insert(4, "Die#5")
            elif discard5.upper() == "N":
                p1_roll["p1_discard_roll1"].insert(4, "No Change")
            # Player1 p1_roll["p1_discard_roll1"] = p1_roll.get("p1_discard_roll1")
            print("Roll1 Discards: ", p1_roll.get("p1_discard_roll1"))
            logger.info("Roll1 Discards:: %s", p1_roll.get("p1_discard_roll1"))
            print("Please enter either [Y/N] to proceed.  To exit enter CTRL-Z: ")
            save_choice1 = input("Are you satisfied with you discards? [Y/N]: ")
            if save_choice1.upper() == "Y":
                # Player1 satisfied with discards.  Calling score()
                # TODO reset p1_roll["p1_rollNumber"] after scoring.
                # print("Function bd_score() called successfully")
                # logger.info("Function bd_score() called successfully")
                # roll_number = roll_number + 1
                print("Function complete_reroll() called from make_choice()")
                logger.info("Function complete_reroll() called from make_choice()")
                save_choice1 = ""
                complete_reroll()
            elif save_choice1.upper() == "N":
                # Player1 notsatisfied with discards.  Calling make_choice()
                print("Function make_choice() called successfully")
                logger.info("Function make_choice() called successfully")
                save_choice1 = ""
                make_choice()
    elif roll_number == 2:
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
            p1_roll["p1_discard_roll2"].insert(0, "Die#1")
        elif discard1.upper() == "N":
            p1_roll["p1_discard_roll2"].insert(0, "No Change")
        if discard2.upper() == "Y":
            # Player wishes to reroll die2
            print("Die# 2")
            okay_to_reroll[1] = discard2.upper()
            p1_roll["p1_discard_roll2"].insert(1, "Die#2")
        elif discard2.upper() == "N":
            p1_roll["p1_discard_roll2"].insert(1, "No Change")
        if discard3.upper() == "Y":
            # Player wishes to reroll die3
            print("Die# 3")
            okay_to_reroll[2] = discard3.upper()
            p1_roll["p1_discard_roll2"].insert(2, "Die#3")
        elif discard3.upper() == "N":
            p1_roll["p1_discard_roll2"].insert(2, "No Change")
        if discard4.upper() == "Y":
            # Player wishes to reroll die4
            print("Die# 4")
            okay_to_reroll[3] = discard4.upper()
            p1_roll["p1_discard_roll2"].insert(3, "Die#4")
        elif discard4.upper() == "N":
            p1_roll["p1_discard_roll2"].insert(3, "No Change")
        if discard5.upper() == "Y":
            # Player wishes to reroll die5
            print("Die# 5")
            okay_to_reroll[4] = discard5.upper()
            p1_roll["p1_discard_roll2"].insert(4, "Die#5")
        elif discard5.upper() == "N":
            p1_roll["p1_discard_roll2"].insert(4, "No Change")
        # Player1 [p1] discard_roll1 = p1_roll.get("p1_discard_roll1")
        print("Roll2 Discards: ", p1_roll.get("p1_discard_roll2"))
        logger.info("Roll2 Discards:: %s", p1_roll.get("p1_discard_roll2"))
        print("Please enter either [Y/N] to proceed.  To exit enter CTRL-Z: ")
        save_choice2 = input("Are you satisfied with you discards? [Y/N]: ")
        if save_choice2.upper() == "Y":
            # Player1 satisfied with discards.  Calling score()
            # TODO reset p1_roll["p1_rollNumber"] after scoring.
            # print("Function bd_score() called successfully")
            # logger.info("Function bd_score() called successfully")
            # roll_number = roll_number + 1
            print("Function complete_reroll() called from make_choice()")
            logger.info("Function complete_reroll() called from make_choice()")
            save_choice2 = ""
            complete_reroll()
        elif save_choice2.upper() == "N":
            # Player1 notsatisfied with discards.  Calling make_choice()
            print("Function make_choice() called successfully")
            logger.info("Function make_choice() called successfully")
            save_choice2 = ""
            make_choice()
#         choice = input("Please enter either [Y/N].  To exit enter CTRL-Z: ")
#         if choice.upper() == "Y":
#             print("Function complete_reroll() called successfully")
#             logger.info("Function complete_reroll() called successfully")
#             complete_reroll()
#         elif choice.upper() == "N":
#             print("Function roll() called successfully")


def complete_reroll():
    """Finalize the reroll of die."""
    import bd_score
    global roll_number
    """
    The function takes no parameters.

    The function does not return any values.

    The function first checks if the user wants to discard the first die
    (discard1) by checking if discard1 is equal to "Y" (case-insensitive)
    . If so, it generates a random number between 1 and 6 (inclusive)
    and assigns it to p1_die1.

    The function then checks if the user wants to discard the second die
    (discard2) by checking if discard2 is equal to "Y" (case-insensitive).
    If so, it generates a random number between 1 and 6 (inclusive) and
    assigns it to p1_die2.


    The function continues this process for the remaining dice (discard3,
    discard4, and discard5), generating a random number for each die if the
    user wants to discard it.

    Finally, the function calls the roll() function to initiate the next round
    of gameplay.

    Note: The global variables discard1, discard2, discard3, discard4, and
    discard5 are assumed to be defined and accessible from within the function.
    """
    print("Function complete_reroll() called successfully")
    logger.info("Function complete_reroll() called successfully")

    global discard1, discard2, discard3, discard4, discard5
    if discard1.upper() == "Y":
        p1_roll["player_die1"] = random.randint(1, 6)
    if discard2.upper() == "Y":
        p1_roll["p1_die2"] = random.randint(1, 6)
    if discard3.upper() == "Y":
        p1_roll["p1_die3"] = random.randint(1, 6)
    if discard4.upper() == "Y":
        p1_roll["p1_die4"] = random.randint(1, 6)
    if discard5.upper() == "Y":
        p1_roll["p1_die5"] = random.randint(1, 6)

    # First roll for player1.
    if roll_number == 1:
        discard1, discard2, discard3, discard4, discard5 = "", "", "", "", ""
        print("roll_number: ", roll_number)
        p1_roll["second_roll_list"] = [p1_roll.get("p1_die1"),
                                       p1_roll.get("p1_die2"),
                                       p1_roll.get("p1_die3"),
                                       p1_roll.get("p1_die4"),
                                       p1_roll.get("p1_die5")]
        print("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"),
              "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"),
              "|", p1_roll.get("p1_die5"), "|")
        logger.info("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"),
                    "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"),
                    "|", p1_roll.get("p1_die5"), "|")
        print("Function secondRoll() being called from complete_reroll()")
        logger.info("Function SecondRoll() being called from complete_reroll()")
        roll_number = roll_number + 1
        secondRoll()
    # Second roll for player1.
    elif roll_number == 2:
        discard1, discard2, discard3, discard4, discard5 = "", "", "", "", ""
        # Second roll for player1
        print("roll_number: ", roll_number)
        p1_roll["second_roll_list"] = [p1_roll.get("p1_die1"), p1_roll.get("p1_die2"), p1_roll.get("p1_die3"),  p1_roll.get("p1_die4"), p1_roll.get("p1_die5")]
        print("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"), "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"), "|", p1_roll.get("p1_die5"), "|")
        logger.info("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"), "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"), "|", p1_roll.get("p1_die5"), "|")
        print("Function lastRoll() being called from complete_reroll()")
        logger.info("Function lastRoll() being called from complete_reroll()")
        roll_number = roll_number + 1
        lastRoll()
    # Final roll for player1.
    elif roll_number == 3:
        # Last roll for player1
        print("roll_number: ", roll_number)
        p1_roll["last_roll_list"] = [p1_roll.get("p1_die1"), p1_roll.get("p1_die2"), p1_roll.get("p1_die3"),  p1_roll.get("p1_die4"), p1_roll.get("p1_die5")]
        print("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"), "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"), "|", p1_roll.get("p1_die5"), "|")
        logger.info("|", p1_roll.get("p1_die1"), "|", p1_roll.get("p1_die2"), "|", p1_roll.get("p1_die3"), "|",  p1_roll.get("p1_die4"), "|", p1_roll.get("p1_die5"), "|")
        print("Function bd_score() being called from complete_reroll()")
        logger.info("Function battleDice_score() being called from complete_reroll()")
        bd_score.battleDice_score(p1_roll.get("lastRollList"))
        print(bd_score.score_choice.get("p1_scorecard"))
        sleep(10)
        if bd_score.game_status == "In Progress":
            play()


if __name__ == "__main__":
    reset_roll()
    play()
