# my_yahtzee.py
# initialize 5 dice for each player
import random
class My_yahtzee:
    player1_roll = {
                'player1_name': "",
                'player1_die1': 0,
                'player1_die2': 0,
                'player1_die3': 0,
                'player1_die4': 0,
                'player1_die5': 0,
                'player1_rollNumber': 1,
                'player1_firstRollList': [],
                'player1_discard_roll1': [],
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
    
    def __init__(self, player_name):
        self.player_name = player_name
       
    @classmethod(My_yahtzee)
    def player1_scorecard(self):
        print("Ones: ", self.player1_ones)
        print("Twos: ", self.player1_twos)
        print("Threes :", self.player1_threes)
        print("Fours: ", self.player1_fours)
        print("Fives: ", self.player1_fives)
        print("Sixes: ", self.player1_sixes)
        print("Upper Total: ", self.player1_upperTotal)
        print("Upper Bonus:", self.player1_upperBonus)
        print("Upper Total: ", self.player1_upperTotal)
        print("3 of a Kind: ", self.player1_3ofaKind)
        print("4 of a Kind: ", self.player1_4ofaKind)
        print("Full House: ", self.player1_fullHouse)
        print("Small Straight: ", self.player1_smallStraight)
        print("Large Straight: ", self.player1_largeStraight)
        print("Yahtzee: ", self.player1_yahtzee)
        print("Chance: ", self.player1_chance)
        print("Lower Total: ", self.player1_lowerTotal)
        print("Total: ", self.player1_total)


    @classmethod(My_yahtzee)
    def play(self):
        self.roll()
        self.score()

    
    

    @classmethod
    def score(self):
        print('Score() called')
#         if self.player1_rollNumber == 1:
#             print("How would you like to score your dice?: ") 
#             self.player1_firstRoll[0]  = self.player1_die1
#             self.player1_firstRoll[1] = self.player1_die2  
#             self.player1_firstRoll[2] = self.player1_die3  
#             self.player1_firstRoll[3] = self.player1_die4  
#             self.player1_firstRoll[4] = self.player1_die5
#             print("player1_first_roll: ", self.player1_firstRoll)
#         
# 
#     
#         print("Enter[1] to score Ones:")
#         print("Enter[2] to score Twos: ")
#         print("Enter[3] to score Threes: ")
#         print("Enter[4] to score Fours: ")
#         print("Enter[5] to score Fives: ")
#         print("Enter[6] to score Sixes: ")
#         print("Enter[T] to score a Three of a Kind: ")
#         print("Enter[F] to score a Four of a Kind: ")
#         print("Enter[FH] to score a Full House: ")
#         print("Enter[S] to score a Small Stright House: ")
#         print("Enter[L] to score a Large Straight: ")
#         print("Enter[C] to score a Chance: ")
#         print("Enter[Z] to score a Yahtzee: ")
#     
#         self.player1_firstRollList = (self.player1_die1, self.player1_die2, self.player1_die3, self.player1_die4, self.player1_die5)
#         print(self.player1_roll.player1_firstRollList)
#         score_choice = input("Please choose one of the above options: ")
#         if score_choice.upper() == "1":
#             self.player1_ones = self.player1_firstRollList.count(1)
#             print("self.player1_ones", self.player1_ones)
#             self.player1_scorecard()
#         elif score_choice.upper() == "2":
#             self.player1_twos = self.player1_firstRollList.count(2) * 2
#             print("self.player1_twos", self.player1_twos)
#         elif score_choice.upper() == "3":
#             self.player1threes = self.player1_firstRollList.count(3) * 3
#             print("self.player1_threes", self.player1_threes)
#         elif score_choice.upper() == "4":
#             self.player1_fours = self.player1_firstRollList.count(4) * 4
#             print("self.player1_fours", self.player1_fours)
#         elif score_choice.upper() == "5":
#             self.player1_fives = self.player1_firstRollList.count(5) * 5
#             print("self.player1_fives", self.player1_fives)
#         elif score_choice.upper() =="6":
#             self.player1_sixes = self.player1_firstRollList.count(6) * 6
#             print("self.player1_sixes", self.player1_sixes)
# 
#         elif score_choice.upper() == "T":
#             for i in self.player1_firstRollList:
#                 self.player1_3ofaKind == self.player1_3ofaKind + i
#             print("You scored a 3o f a Kind: ", self.player1_3ofaKind)
#         elif score_choice.upper() == "F":
#             for i in self.player1_firstRollList:
#                 self.player1_4ofaKind == self.player1_4ofaKind + i
#             print("You scored a 4 of a kind: ", self.player1_4ofaKind)
#         elif score_choice.upper() == "FH":
#             self.player1_fullHouse = 25
#             print("You scored a Full House: ", self.player1_fullHouse)
#         elif score_choice.upper() == "S":
#             self.player1_SmallStraight = 30
#             print("You scored Small Straight: ", self.player1_smallStraight)
#         elif score_choice.upper() == "L":
#             self.player1_LargeStraight = 40
#             print("You scored a Large Straight: ", self.player1_largeStraight)
#         elif score_choice.upper() == "S":
#             self.player1_yahtzee = 50
#             print("You scored a Yahtzee: ", self.player1_yahtzee)
#         elif score_choice.upper() == "C":
#             for i in self.player1_firstRollList:
#                 self.player1_chance = self.player1_chance + i   
#             print("You scored a Chance: ", self.player1_chance)
#     
#             print("printing player1 scorecard")
#             self.player1_scorecard()
# 



        # elif self.player1_card["Twos"] = 0
        #     self.player1_card["Threes"] = 0
        #     self.player1_card["Fours"] = 0
        #     self.player1_card["Fives"] = 0
        #     self.player1_card["Sixes"] = 0

    @classmethod(My_yahtzee)
    def roll(self):
        if self.player1_roll.get('player1_rollNnumber') == 1:
            '''Initial roll of the dice'''
            self.player1_roll.player1_die1 = random.randint(1,6)
            self.player1_roll.player1_die2 = random.randint(1,6)
            self.player1_roll.player1_die3 = random.randint(1,6)
            self.player1_roll.player1_die4 = random.randint(1,6)
            self.player1_roll.player1_die5 = random.randint(1,6)
            print("You rolled.....")
            self.player1_roll.player1_firstRollList = [
                self.player1_roll.player1_die1,
                self.player1_roll.player1_die2,
                self.player1_roll.player1_die3,
                self.player1_roll.player1_die4,
                self.player1_roll.player1_die5
                ]
                
             #show hand to player
            print("|", self.player1_roll.player1_die1, "|", self.player1_roll.player1_die2, "|", self.player1_roll.player1_die3, "|",  self.player1_roll.player1_die4, "|", self.player1_roll.player1_die5)
            print()
            keep1 = input("Would you like to discard any die?: ")
            if keep1.upper() == "N":
                self.score()
                return self.player1_roll.player1_die1, self.player1_roll.player1_die2, self.player1_roll.player1_die3, self.player1_roll.player1_die4, self.player1_roll.player1_die5
            
    def make_choice(self):
        '''Give player opportunity to modify roll.'''
        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        self.player1_roll.discard_roll1 = [discard1, discard2, discard3, discard4, discard5]
        if discard1.upper() == "Y":
            print('Die# 1')
        elif discard2.upper() == "Y":
                print('Die# 2')
        elif discard3.upper() == "Y":
                print('Die# 3')
        elif discard4.upper() == "Y":
                print('Die# 4')
        elif discard5.upper() == "Y":
                print('Die# 5')
# put in confirmation if == "N" go back to choice
            self.player1_die1 =random.randint(1,6)
            print()
        if discard2.upper() == "Y":
           self.player1_die2 = random.randint(1,6)
           print()
        if discard3.upper() == "Y":
            print('Die# 3')
        self.player1_die3 = random.randint(1,6)
            print()
        if discard4.upper() == "Y":
            print('Die# 4')
            self.player1_die4 = random.randint(1,6)
            print()
        if discard5.upper() == "Y":
            self.player1_die5 = random.randint(1,6)
            print()


        print(self.player1_name, "Your hand: ")
        print(self.player1_die1, self.player1_die2, self.player1_die3, self.player1_die4, self.player1_die5)
        print()
          #  elif self.player1_rollNumber == 3:
            # do not allow for discard of unwanted die.N
           # pass



        keep2 = input("Would you like to discard any die?: ")
        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")

        if keep2.upper() == "N":
            self.score()
        if discard1.upper() == "Y":
            self.player1_die1 =random.randint(1,6)
            print()
        if discard2.upper() == "Y":
           self.player1_die2 = random.randint(1,6)
           print()
        if discard3.upper == "Y":
            self.player1_die3 = random.randint(1,6)
            print()
        if discard4.upper() == "Y":
            self.player1_die4 = random.randint(1,6)
            print()
        if discard5.upper() == "Y":
            self.player1_die5 = random.randint(1,6)
            print()

        print()
        print(My_yahtzee.player1_name, "Your hand: ")
        print("|", self.player1_die1, "|", self.player1_die2, "|", self.player1_die3, "|",  self.player1_die4, "|", self.player1_die5)
        print()
        print("Would you like to score your points or roll again?")
        score_or_roll = input("Please enter (s) to score now or (r) to roll again.")
        
        if score_or_roll.upper() == "S":
            self.score()
        elif score_or_roll.upper() == "R":
            self.player1_rollNumber = self.player1_rollNumber + 1
            self.roll()
        else:
            print("Invalid Selection.  Please choose again.")
        print()
        self.player1_name = self.player1_name
        print(self.player1_name)
        print("|", self.player1_die1, "|", self.player1_die2, "|", self.player1_die3, "|",  self.player1_die4,"|",self.player1_die5, "|")
 
    

    


yahtzee1 = My_yahtzee("Tony")
yahtzee1.roll()

