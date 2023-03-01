# my_yahtzee.py
# initialize 5 dice for each player
import random
import user_login
import score
player1_roll = {
            'player1_name': "",
            'player1_die1': 0,
            'player1_die2': 0,
            'player1_die3': 0,
            'player1_die4': 0,
            'player1_die5': 0,
            'player1_rollNumber': 1,
            'player1_firstRollList': [],
            'player1_secondRollList': [],
            'player1_discard_roll1': [],
            'player1_thirdRollList': []
            }

# player1 scorecard
player1_scorecard = {
                'player1_ones': 0,
                'player1_twos': 0,
                'player1_threes': 0,
                'player1_fours': 0,
                'player1_fives': 0,
                'player1_sixes': 0,
                'player1_upperTotal': 0,
                'player1_upperBonus': 0,
                'player1_upperTotal': 0,
                'player1_3ofaKind': 0,
                'player1_4ofaKind': 0,
                'player1_fullHouse': 0,
                'player1_smallStraight': 0,
                'player1_largeStraight': 0,
                'player1_yahtzee': 0,
                'player1_chance': 0,
                'player1_lowerTotal': 0,
                'player1_total': 0
                }
# Player2 roll
player2_roll = {
                'player2_name': "",
                'player2_die1': 0,
                'player2_die2': 0,
                'player2_die3': 0,
                'player2_die4': 0,
                'player2_die5': 0,
                'player2_rollNumber': 1,
                'player2_firstRollList': [],
                'player2_discard_roll1': [],
                'player2_secondRollList': [],
                'player2_discard_roll2': [],
                'player2_thirdRollList': []
                }
            
#player2_scorecard
player2_scorecard  = {
               'player2_ones': 0,
                'player2_twos': 0,
                'player2_threes': 0,
                'player2_fours': 0,
                'player2_fives': 0,
                'player2_sixes': 0,
                'player2_upperTotal': 0,
                'player2_upperBonus': 0,
                'player2_upperTotal': 0,
                'player2_3ofaKind': 0,
                'player2_4ofaKind': 0,
                'player2_fullHouse': 0,
                'player2_smallStraight': 0,
                'player2_largeStraight': 0,
                'player2_yahtzee': 0,
                'player2_chance': 0,
                'player2_lowerTotal': 0,
                'player2_total': 0
                }

   
def player1_scorecard():
    print("Ones: ", player1_ones)
    print("Twos: ", player1_twos)
    print("Threes :", player1_threes)
    print("Fours: ", player1_fours)
    print("Fives: ", player1_fives)
    print("Sixes: ", player1_sixes)
    print("Upper Total: ", player1_upperTotal)
    print("Upper Bonus:", player1_upperBonus)
    print("Upper Total: ", player1_upperTotal)
    print("3 of a Kind: ", player1_3ofaKind)
    print("4 of a Kind: ", player1_4ofaKind)
    print("Full House: ", player1_fullHouse)
    print("Small Straight: ", player1_smallStraight)
    print("Large Straight: ", player1_largeStraight)
    print("Yahtzee: ", player1_yahtzee)
    print("Chance: ", player1_chance)
    print("Lower Total: ", player1_lowerTotal)
    print("Total: ", player1_total)


def play():
    roll()
    score()


    
        # elif player1_card["Twos"] = 0
        #     player1_card["Threes"] = 0
        #     player1_card["Fours"] = 0
        #     player1_card["Fives"] = 0
        #     player1_card["Sixes"] = 0

def roll():
    if player1_roll.get('player1_rollNnumber') == 1:
        '''Initial roll of the dice'''
        player1_roll.player1_die1 = random.randint(1,6)
        player1_roll.player1_die2 = random.randint(1,6)
        player1_roll.player1_die3 = random.randint(1,6)
        player1_roll.player1_die4 = random.randint(1,6)
        player1_roll.player1_die5 = random.randint(1,6)
        print("You rolled.....")
        
        player1_roll.player1_firstRollList = [
        player1_roll.player1_die1,
        player1_roll.player1_die2,
        player1_roll.player1_die3,
        player1_roll.player1_die4,
        player1_roll.player1_die5
        ]
            
         #show hand to player
        print("|", player1_roll.player1_die1, "|", player1_roll.player1_die2, "|", player1_roll.player1_die3, "|",  player1_roll.player1_die4, "|", player1_roll.player1_die5)
        print()
        keep1 = input("Would you like to discard any die?: ")
        if keep1.upper() == "N":
            score()
            return player1_roll.player1_die1, player1_roll.player1_die2, player1_roll.player1_die3, player1_roll.player1_die4, player1_roll.player1_die5
        
def make_choice():
    '''Give player opportunity to modify roll.'''
    discard1 = input("Would you like to discard die1? Y for Yes:")
    discard2 = input("Would you like to discard die2? Y for Yes:")
    discard3 = input("Would you like to discard die3? Y for Yes:")
    discard4 = input("Would you like to discard die4? Y for Yes:")
    discard5 = input("Would you like to discard die5? Y for Yes:")
    okay_to_reroll = []
    if discard1.upper() == "Y":
        print('Die# 1')
        okay_to_reroll[0] = discard1.upper()
    if discard2.upper() == "Y":
        print('Die# 2')
        okay_to_reroll[1] = discard2.upper()
     if discard3.upper() == "Y":
        print('Die# 3')
        okay_to_reroll[2] = discard3.upper()
    if discard4.upper() == "Y":
        print('Die# 4')
        okay_to_reroll[3]  = discard4.upper()
    if discard5.upper() == "Y":
        print('Die# 5')
        okay_to_reroll[4] = discard5.upper()
       # put in confirmation if == "N" go back to choice
       print("You okay with reroll status?")
    reroll_check = input("Enter [Y] to continue with reroll or [N] to re-select the die: ")
    if reroll_check.upper() == "Y":
        complete_reroll()
    elif reroll_check.upper() =  "N":
        make_choice()
    else:
        print("Please enter either [Y] or [N].  To exit enter CTRL-Z: ")
        make_choice()
            
def complete_reroll():
    if discard1.upper() == "Y":
        player1_die1 = random.randint(1,6)
    if discard2.upper() == "Y":
        player1_die2 = random.randint(1,6)
    if discard3.upper() == "Y":
        player1_die3 = random.randint(1,6)
    if discard4.upper() == "Y":
        player1_die4 = random.randint(1,6)
    if discard5.upper() == "Y":
        player1_die5 = random.randint(1,6)
   roll()

