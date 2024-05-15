# bd_score.py
import BattleDice
import logging
from time import sleep
import sys
logger = logging.getLogger("bd_logger")
logging.basicConfig(filename="C:\\Projects\\BattleDice\\Logs\\BattleDice.log",
                    encoding="utf-8",
                    filemode="a", 
                    format='%(asctime)s %(levelname)s | %(name)s | %(lineno)d | %(funcName)s | %(message)s', 
                    datefmt='%Y.%m.%d %I:%M:%S %p', 
                    level=logging.DEBUG)

pl_score = {}
scoring_list = []
dice = []
game_status = "In Progress" 
round_score = 0
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

p2_scorecard  = {
                "p2_ones": 0,
                "p2_twos": 0,
                "p2_threes": 0,
                "p2_fours": 0,
                "p2_fives": 0,
                "p2_sixes": 0,
                "p2_upperTotal": 0,
                "p2_upperBonus": 0,
                "p2_upperTotal": 0,
                "p2_3ofaKind": 0,
                "p2_4ofaKind": 0,
                "p2_fullHouse": 0,
                "p2_smallStraight": 0,
                "p2_largeStraight": 0,
                "p2_bunkerBuster": 0,
                "p2_chance": 0,
                "p2_lowerTotal": 0,
                "p2_total": 0
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
    
    print("Ones: ", score_choice.p1_scorecard.get("p1_ones")) #p1_ones
    print("Twos: ", score_choice.p1_scorecard.get("p1_twos")) #p1_twos
    print("Threes :", score_choice.p1_scorecard.get("p1_threes")) #p1_threes
    print("Fours: ", score_choice.p1_scorecard.get("p1_fours")) #p1_fours
    print("Fives: ", score_choice.p1_scorecard.get("p1_fives")) #p1_fives
    print("Sixes: ", score_choice.p1_scorecard.get("p1_sixes")) #p1_sixes
    print("Upper Total: ", score_choice.p1_scorecard.get("p1_upperAmount")) #p1_upperAmount
    print("Upper Bonus:", score_choice.p1_scorecard.get("p1_upperBonus")) #p1_upperBonus
    print("Upper Total: ", score_choice.p1_scorecard.get("p1_upperTotal")) #p1_upperTotal
    print("3 of a Kind: ", score_choice.p1_scorecard.get("p1_3ofaKind")) #p1_3ofaKind
    print("4 of a Kind: ", score_choice.p1_scorecard.get("p1_4ofaKind")) #p1_4ofaKind
    print("Full House: ", score_choice.p1_scorecard.get("p1_fullHouse")) #p1_fullHouse
    print("Small Straight: ", score_choice.p1_scorecard.get("p1_smallStraight")) #p1_smallStraight
    print("Large Straight: ", score_choice.p1_scorecard.get("p1_largeStraight")) #p1_largeStraight
    print("Bunker Buster: ", score_choice.p1_scorecard.get("player1bunkerBuster")) #p1_bunkerBuster
    print("Chance: ", score_choice.p1_scorecard.get("p1_chance")) #p1_chance
    print("Lower Total: ", score_choice.p1_scorecard.get("p1_lowerTotal")) #p1_lowerTotal
    print("Total: ", score_choice.p1_scorecard.get("p1_total")) #p1_total
    logger.info("Function print_p1_scorecard() completed successfully")

def print_p2_scorecard():
    """
    Print the scorecard for player 2.

    This function prints out the scores for each category on the scorecard
    for player 2.

    Args:
        p2_ones -> int
        p2_twos -> int
        p2_threes -> int
        p2_fours -> int
        p2_fives -> int
        p2_sixes -> int
        p2_upperTotal -> int
        p2_upperBonus -> int
        p2_3ofaKind -> int
        p2_4ofaKind -> int
        p2_fullHouse -> int
        p2_smallStraight -> int
        p2_largeStraight -> int
        p2_bunkerBuster -> int
        p2_chance -> int
        p2_lowerTotal -> int
        p2_total -> int

    Returns:
        None
    """
    print("Ones: ", p2_scorecard.get("p2_ones")) #p2_ones
    print("Twos: ", p2_scorecard.get("p2_twos")) #p2_twos
    print("Threes :", p2_scorecard.get("p2_threes")) #p2_threes
    print("Fours: ", p2_scorecard.get("p2_fours")) #p2_fours
    print("Fives: ", p2_scorecard.get("p2_fives")) #p2_fives
    print("Sixes: ", p2_scorecard.get("p2_sixes")) #p2_sixes
    print("Upper Total: ", p2_scorecard.get("p2_upperAmount")) #p2_upperAmount
    print("Upper Bonus:", p2_scorecard.get("p2_upperBonus")) #p2_upperBonus
    print("Upper Total: ", p2_scorecard.get("p2_upperTotal")) #p2_upperTotal
    print("3 of a Kind: ", p2_scorecard.get("p2_3ofaKind")) #p2_3ofaKind
    print("4 of a Kind: ", p2_scorecard.get("p2_4ofaKind")) #p2_4ofaKind
    print("Full House: ", p2_scorecard.get("p2_fullHouse")) #p2_fullHouse
    print("Small Straight: ", p2_scorecard.get("p2_smallStraight")) #p2_smallStraight
    print("Large Straight: ", p2_scorecard.get("p2_largeStraight")) #p2_largeStraight
    print("Bunker Buster: ", p2_scorecard.get("p2_bunkerBuster")) #p2_BunkerBuster
    print("Chance: ", p2_scorecard.get("p2_chance")) #p2_chance
    print("Lower Total: ", p2_scorecard.get("p2_lowerTotal")) #p2_lowerTotal
    print("Total: ", p2_scorecard.get("p2_total")) #p2_total
    logger.info("Function print_p2_scorecard() completed successfully")

def game_over():

    p1_scorecard["ones"] = 0
    p1_scorecard["twos"] = 0
    p1_scorecard["threes"] = 0
    p1_scorecard["fours"] = 0
    p1_scorecard["fives"] = 0
    p1_scorecard["sixes"] = 0
    p1_scorecard["upperTotal"] = 0
    p1_scorecard["upperBonus"] = 0
    p1_scorecard["3ofaKind"] = 0
    p1_scorecard["4ofaKind"] = 0
    p1_scorecard["fullHouse"] = 0
    p1_scorecard["smallStraight"] = 0
    p1_scorecard["largeStraight"] = 0
    p1_scorecard["bunkerBuster"] = 0
    p1_scorecard["chance"] = 0
    p1_scorecard["lowerTotal"] = 0
    p1_scorecard["total"] = 0
    p2_scorecard["ones"] = 0
    p2_scorecard["twos"] = 0
    p2_scorecard["threes"] = 0
    p2_scorecard["fours"] = 0
    p2_scorecard["fives"] = 0
    p2_scorecard["sixes"] = 0
    p2_scorecard["upperTotal"] = 0
    p2_scorecard["upperBonus"] = 0
    p2_scorecard["3ofaKind"] = 0
    p2_scorecard["4ofaKind"] = 0
    p2_scorecard["fullHouse"] = 0
    p2_scorecard["smallStraight"] = 0
    p2_scorecard["largeStraight"] = 0
    p2_scorecard["bunkerBuster"] = 0
    p2_scorecard["chance"] = 0
    p2_scorecard["lowerTotal"] = 0
    p2_scorecard["total"] = 0


def battleDice_score(dice):
    # Get list of possible scoring opportunitie
    global scoring_list
    scoring_list= []
    # Count the occurrences of each number in the roll
    counts = [dice.count(i) for i in range(1, 7)]
    if counts[0] > 0: # Check for Ones
        scoring_list.append("Ones")

    if counts[1] > 0: # Check for Twos
        scoring_list.append("Twos")
    
    if counts[2] > 0: # Check for Threes
        scoring_list.append("Threes")
    
    if counts[3] > 0: # Check for Fours
        scoring_list.append("Fours")
    
    if counts[4] > 0: # Check for Fives
        scoring_list.append("Fives")
    
    if counts[5] > 0: # Check for Sixes
        scoring_list.append("Sixes")
    
    # Check for Yahtzee (all dice are the same)
    if max(counts) == 5:
        # Die equals 5 of a kind.  EX: 5 5 5 5 5
        # Append to scoring_list for customer scoring option
        scoring_list.append("Bunker Buster") # Yahtzee
        #return "Bunker Buster / Yahtzee!"
    
    # Check for Four of a Kind
    if max(counts) >= 4:
        # Die equals or is greater than 4 of a kind.  EX: 5 5 5 5 6
        # Append to scoring_list for customer scoring option
        scoring_list.append("Four of a Kind")
        #return "Four of a Kind"
    
    # Check for Full House
    if 2 in counts and 3 in counts:
        # Die equals 3 of a kind and remaing die are the same.  EX: 5 5 2 2 2
        # Append to scoring_list for customer scoring option
        scoring_list.append("Full House")
        # return "Full House"

    # Check for Three of a Kind
    if max(counts) >= 3:   # Die equals 5 of a kind.  EX: 5 5 5 5 5
        # Append to scoring_list for customer scoring option
        scoring_list.append("Three of a Kind")
        #
    # return "Three of a Kind"
    
    # Check for Small Straight
    if counts == [1, 1, 1, 1, 0, 0] or counts == [0, 1, 1, 1, 1, 0] or counts == [0, 0, 1, 1, 1, 1] \
    or counts == [2, 1, 1, 1, 0, 0] or counts == [0, 2, 1, 1, 1, 0] or counts == [0, 0, 1, 2, 1, 1] \
    or counts == [1, 2, 1, 1, 0, 0] or counts == [0, 1, 2, 1, 1, 0] or counts == [0, 0, 2, 1, 1, 1] \
    or counts == [1, 1, 2, 1, 0, 0] or counts == [0, 1, 1, 2, 1, 0] or counts == [0, 0, 1, 1, 2, 1] \
    or counts == [1, 1, 1, 2, 0, 0] or counts == [0, 1, 1, 1, 2, 0] or counts == [0, 0, 1, 1, 1, 2]:
        
        scoring_list.append("Small Straight")
        
        #return "Small Straight"
        
    
    # Check for Large Straight
    print("counts: ", counts)
    if counts == [0, 1, 1, 1, 1, 1] or  counts == [ 1, 1, 1, 1, 1, 0]:
        scoring_list.append("Large Straight")
        #return "Large Straight"
    
    # scoring_list.append("Chance") always add to scoring_list.  
    # scorecard parser will clean out the remaining options
    scoring_list.append("Chance")

    logger.info("scoring_list: %s", scoring_list)
    print("Scoring_List: ", scoring_list)
    score_choice(scoring_list)

def score_choice(scoring_list):
    global dice
    global counts
    global roll_number
    global p1_scorecard
    global game_status
    global round_score
    game_status = "In Progress"
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
    # Check for to score Ones. aka snake eyes.
    for score_item in scoring_list:
        if score_item == "Ones" and p1_scorecard.get("p1_ones") == 0:
            choice_ones = input("Would you like to score the ones? [Y/N] ")
            if choice_ones.upper == "Y":
                p1_scorecard["p1_ones"] = counts[0]
                print(p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_ones")
                print("Scoring Ones for ", counts[0], " points!")
                logger.info("Scoring Ones for  {ones_score}  points!")
            break
        if score_item == "Twos" and p1_scorecard.get("p1_twos") == 0:
            choice_twos = input("Would you like to score the twos? [Y/N] ")
            if choice_twos.upper == "Y":
                p1_scorecard["p1_twos"] = counts[1] * 2
                print(p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_twos")
                print("Scoring Twos for ", counts[1] * 2, " points!")
                logger.info("Scoring Twos for ", counts[1] * 2, " points!")
            break
        if score_item == "Threes" and p1_scorecard.get("p1_threes") == 0:
            choice_threes = input("Would you like to score the threes? [Y/N] ")
            if choice_threes.upper == "Y":
                p1_scorecard["p1_threes"] = counts[2] * 3
                print(print_p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_threes")
                print("Scoring Threes for ", counts[2] * 3, " points!")
                logger.info("Scoring Threes for ", counts[2] * 3, " points!")
            break
        if score_item == "Fours" and p1_scorecard.get("p1_fours") == 0:
            choice_fours = input("Would you like to score the fours? [Y/N] ")
            if choice_fours.upper == "Y":        
                p1_scorecard["p1_fours"] = counts[3] * 4
                print(print_p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_fours")
                print("Scoring Fours for ", counts[3] * 4, " points!")
                logger.info("Scoring Ones for ", counts[3] * 4, " points!")
            break
        if score_item == "Fives" and p1_scorecard.get("p1_fives") == 0:
            choice_fives = input("Would you like to score the fives? [Y/N] ")
            if choice_fives.upper == "Y":
                p1_scorecard["p1_fives"] = counts[4] * 5
                print(print_p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_fives")
                print("Scoring Fives for ", counts[4] * 5, " points!")
                logger.info("Scoring Fives for ", counts[4] * 5, " points!")
            break
        if score_item == "Sixes" and p1_scorecard.get("p1_sixes") == 0:
            choice_sixes = input("Would you like to score the sixes? [Y/N] ")
            if choice_sixes.upper == "Y":
                p1_scorecard["p1_sixes"] = counts[5] * 6
                print(print_p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_sixes")
                print("Scoring Sixes for ", counts[5] * 6, " points!")
                logger.info("Scoring Sixes for ", counts[5] * 6, " points!")
            break

        if score_item == "BunkerBuster" and p1_scorecard.get("p1_bunker_buster") == 0:
            choice_bunker_buster = input("Would you like to score the bunker_buster? [Y/N] ")
            if choice_bunker_buster.upper == "Y":
                p1_scorecard["p1_bunker_buster"] = 50
                print(print_p1_scorecard())
                roll_number = 1
                scoring_list = []
                round_score = p1_scorecard.get("p1_bunker_buster")
                print("Scoring Bunker Buster for 50 points!")
                logger.info("Scoring Bunker Buster for 50 points!")
            break            

        if score_item == "4 of a Kind" and p1_scorecard.get("p1_4ofAKind") == 0:
            choice_4OfAKind = input("Would you like to score the 4 of a Kind? [Y/N] ")
            if choice_4OfAKind.upper == "Y":
                p1_scorecard["p1_4ofAKind"] = sum(dice)
                print(print_p1_scorecard())
                roll_number = 1
                sleep(10)
                scoring_list = []
                round_score = p1_scorecard.get("p1_4ofAKind")
                print("Scoring four of akind for", score_choice.p1_scorecard.get("p1_4ofAKind"), "points!")
                logger.info("Scoring four of akind for", score_choice.p1_scorecard.get("p1_4ofAKind"), "points!")
            break
            
        if score_item == "3 of a Kind" and p1_scorecard.get("p1_3ofAKind") == 0:
            choice_3OfAKind = input("Would you like to score the 3 of a Kind? [Y/N] ")
            if choice_4OfAKind.upper == "Y":
                p1_scorecard["p1_3ofAKind"] = sum(dice)
                print(print_p1_scorecard())
                roll_number = 1
                sleep(10)
                scoring_list = []
                round_score = p1_scorecard.get("p1_3ofAKind")
                print("Scoring three of akind for", score_choice.p1_scorecard.get("p1_3ofAKind"), "points!")
                logger.info("Scoring three of akind for", score_choice.p1_scorecard.get("p1_3ofAKind"), "points!")
            break

        if score_item == "Full House" and p1_scorecard.get("p1_fullHouse") == 0:
            choice_fullHouse = input("Would you like to score the Full House? [Y/N] ")
            if choice_fullHouse.upper == "Y":
                  p1_scorecard["p1_fullHouse"] = sum(dice)
                print(print_p1_scorecard())
                roll_number = 1
                sleep(10)
                scoring_list = []
                round_score = p1_scorecard.get("p1_full_house")
                print("Scoring full_house for", score_choice.p1_scorecard.get("full_house"), "points!")
                logger.info("Scoring full house for", score_choice.p1_scorecard.get("full_house"), "points!")
            break  

    if "Small Straight" in scoring_list and p1_scorecard.get("p1_smallStraight") == 0:
        choice_smallStraight = input("Would you like to score the Small Straight? [Y/N] ")
        if choice_smallStraight.upper == "Y":
            p1_scorecard["p1_smallStraight"] = 30
            print(print_p1_scorecard())
            roll_number = 1
            sleep(10)
            scoring_list = []
            round_score = p1_scorecard.get("p1_smallStraight")
            print("Scoring small straight for", score_choice.p1_scorecard.get("p1_smallStraight"), "points!")
            logger.info("Scoring small straight for", score_choice.p1_scorecard.get("p1_smallStraight"), "points!")
            exit()

    if "Large Straight" in scoring_list and p1_scorecard.get("p1_largeStraight") == 0:
        choice_largeStraight = input("Would you like to score the Large Straight? [Y/N] ")
        if choice_largeStraight.upper == "Y":
            p1_scorecard["p1_largeStraight"] = 30
            print(print_p1_scorecard())
            roll_number = 1
            sleep(10)
            scoring_list = []
            round_score = p1_scorecard.get("large_straight")
            print("Scoring large straight for", score_choice.p1_scorecard.get("large_straight"), "points!")
            logger.info("Scoring large straight for", score_choice.p1_scorecard.get("large_straight"), "points!")
            exit()

    if "Chance" in scoring_list and p1_scorecard.get("p1_chance") == 0:
        choice_chance = input("Would you like to score the Chance? [Y/N] ")
        if choice_chance.upper == "Y":
            p1_scorecard["p1_chance"] = sum(dice)
            print(print_p1_scorecard())
            roll_number = 1
            sleep(10)
            scoring_list = []
            round_score = p1_scorecard.get("p1_chance")
            print("Scoring chance for", score_choice.p1_scorecard.get("p1_chance"), "points!")
            logger.info("Scoring chance for", score_choice.p1_scorecard.get("p1_chance"), "points!")
            exit()

    # elif "Full House" in scoring_list:
    #     return "Full House"
    # elif "Three of a Kind" in scoring_list:
    #     return "Three of a Kind"
    # elif "Small Straight" in scoring_list:
    #     return "Small Straight"
    # elif "Large Straight" in scoring_list:
    #     return "Large Straight"
    # else:
    #     return "Chance"




# Example usage
#roll = [5, 2, 3, 4, 6]
#roll = [1, 2, 3, 4, 5]
#roll = [2, 2, 2, 4, 5]
#roll = [2, 2, 2, 4, 4]
#roll = [2, 2, 2, 5, 5]
#roll = [2, 2, 2, 2, 2]

# score = battleDice_score(roll)
# print(f"The score for the roll {roll} is: {round_score}")

