# my_yahtzee.py
# initialize 5 dice for each player
import random
class My_yahtzee:
    player1_name = ""
    player1_die1 = 0
    player1_die2 = 0
    player1_die3 = 0
    player1_die4 = 0
    player1_die5 = 0
    player1_rollNumber = 1
    player1_firstRoll = {1:0, 2:0, 3:0, 4:0, 5:0}
    player1_firstRollList = ()
    player1_secondRoll = {1:0, 2:0, 3:0, 4:0, 5:0}
    player1_secondRollList = ()
    player1_thirdRoll = {1:0, 2:0, 3:0, 4:0, 5:0}
    player1_thirdRollList = ()

    # player1 scorecard
    player1_ones = 0
    player1_twos = 0
    player1_threes = 0
    player1_fours = 0
    player1_fives = 0
    player1_sixes = 0
    player1_upperTotal = 0
    player1_upperBonus = 0
    player1_upperTotal = 0
    player1_3ofaKind = 0
    player1_4ofaKind = 0
    player1_fullHouse = 0
    player1_smallStraight = 0
    player1_largeStraight = 0
    player1_yahtzee = 0
    player1_chance = 0
    player1_lowerTotal = 0
    player1_total = 0

    player2_name = ""
    player2_die1 = 0
    player2_die2 = 0
    player2_die3 = 0
    player2_die4 = 0
    player2_die5 = 0
    player2_rollNumber = 1

    #player2_scorecard
    player2_ones = 0
    player2_twos = 0
    player2_threes = 0
    player2_fours = 0
    player2_fives = 0
    player2_sixes = 0
    player2_upperTotal = 0
    player2_upperBonus = 0
    player2_upperTotal = 0
    player2_3ofaKind = 0
    player2_4ofaKind = 0
    player2_fullHouse = 0
    player2_smallStraight = 0
    player2_largeStraight = 0
    player2_yahtzee = 0
    player2_chance = 0
    player2_lowerTotal = 0
    player2_total = 0
    
    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
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


    @classmethod
    def play(self):
        self.roll()
        self.score()

    
    

    @classmethod
    def score(self):
        if self.player1_rollNumber == 1:
            print("How would you like to score your dice?: ") 
            self.player1_firstRoll[1]  = self.player1_die1
            self.player1_firstRoll[2] = self.player1_die2  
            self.player1_firstRoll[3] = self.player1_die3  
            self.player1_firstRoll[4] = self.player1_die4  
            self.player1_firstRoll[5] = self.player1_die5
            print("player1_first_roll: ", self.player1_firstRoll)
        

    
        print("Enter[1] to score Ones:")
        print("Enter[2] to score Twos: ")
        print("Enter[3] to score Threes: ")
        print("Enter[4] to score Fours: ")
        print("Enter[5] to score Fives: ")
        print("Enter[6] to score Sixes: ")
        print("Enter[T] to score a Three of a Kind: ")
        print("Enter[F] to score a Four of a Kind: ")
        print("Enter[FH] to score a Full House: ")
        print("Enter[S] to score a Small Stright House: ")
        print("Enter[L] to score a Large Straight: ")
        print("Enter[C] to score a Chance: ")
        print("Enter[Z] to score a Yahtzee: ")
    
        self.player1_firstRollList = (self.player1_die1, self.player1_die2, self.player1_die3, self.player1_die4, self.player1_die5)
        print(self.player1_firstRollList)
        score_choice = input("Please choose one of the above options: ")
        if score_choice.upper() == "1":
            self.player1_ones = self.player1_firstRollList.count(1)
            print("self.player1_ones", self.player1_ones)
        elif score_choice.upper() == "2":
            self.player1_twos = self.player1_firstRollList.count(2) * 2
            print("self.player1_twos", self.player1_twos)
        elif score_choice.upper() == "3":
            self.player1threes = self.player1_firstRollList.count(3) * 3
            print("self.player1_threes", self.player1_threes)
        elif score_choice.upper() == "4":
            self.player1_fours = self.player1_firstRollList.count(4) * 4
            print("self.player1_fours", self.player1_fours)
        elif score_choice.upper() == "5":
            self.player1_fives = self.player1_firstRollList.count(5) * 5
            print("self.player1_fives", self.player1_fives)
        elif score_choice.upper() =="6":
            self.player1_sixes = self.player1_firstRollList.count(6) * 6
            print("self.player1_sixes", self.player1_sixes)

        elif score_choice.upper() == "T":
            for i in self.player1_firstRollList:
                self.player1_3ofaKind == self.player1_3ofaKind + i
            print("self.player1_3ofaKind: ", self.player1_3ofaKind)
        elif score_choice.upper() == "F":
            for i in self.player1_firstRollList:
                self.player1_4ofaKind == self.player1_4ofaKind + i
            print("self.player1_4ofaKind: ", self.player1_4ofaKind)
        elif score_choice.upper() == "FH":
            self.player1_fullHouse = 25
            print("self.player1_fullHouse: ", self.player1_fullHouse)
        elif score_choice.upper() == "S":
            self.player1_SmallStraight = 30
            print("self.player1_smallStraight: ", self.player1_SmallStraight)
        elif score_choice.upper() == "L":
            self.player1_LargeStraight = 40
            print("self.player1_largeStraight: ", self.player1_LargeStraight)
        elif score_choice.upper() == "S":
            self.player1_yahtzee = 50
            print("self.player1_fullHouse: ", self.player1_fullHouse)
        elif score_choice.upper() == "C":
            for i in self.player1_firstRollList:
                self.player1_chance = self.player1_chance + i   
            print("self.player1_chance: ", self.player1_chance)
    
        self.player1_scorecard()




        # elif self.player1_card["Twos"] = 0
        #     self.player1_card["Threes"] = 0
        #     self.player1_card["Fours"] = 0
        #     self.player1_card["Fives"] = 0
        #     self.player1_card["Sixes"] = 0

    @classmethod
    def roll(self):
        if self.player1_rollNumber == 1:
            '''Initial roll of the dice'''
            self.player1_die1 = random.randint(1,6)
            self.player1_die2 = random.randint(1,6)
            self.player1_die3 = random.randint(1,6)
            self.player1_die4 = random.randint(1,6)
            self.player1_die5 = random.randint(1,6)
            print("Hand for", self.player1_name, "after initial roll.")
            print(self.player1_name, "Your hand: ", self.player1_die1, self.player1_die2, self.player1_die3, self.player1_die4, self.player1_die5)
        elif self.player1_rollNumber == 2:
            pass




        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        if discard1.upper() == "Y":
            self.player1_die1 =random.randint(1,6)
        if discard2.upper() == "Y":
           self.player1_die2 = random.randint(1,6)
        if discard3.upper == "Y":
            self.player1_die3 = random.randint(1,6)
        if discard4.upper() == "Y":
            self.player1_die4 = random.randint(1,6)
        if discard5.upper() == "Y":
            self.player1_die5 = random.randint(1,6)


        print("Player Name: ", self.player1_name)
        print("This is your current hand after 2nd roll")
        print(self.player1_name, "Your hand: ", self.player1_die1, self.player1_die2, self.player1_die3, self.player1_die4, self.player1_die5)
        print("Would you like to score your points or roll again?")
        score_or_roll = input("Please enter (s) to score now or (r) to roll again.")
        
        if score_or_roll.upper() == "S":
            self.score()
        elif score_or_roll.upper() == "R":
            self.player1_rollNumber = self.player1_rollNumber + 1
            self.roll()
        else:
            print("Please choose again")
        print()
        self.player1_name = self.player1_name
        print(self.player1_name)
        print("|", self.player1_die1, "|", self.player1_die2, "|", self.player1_die3, "|",  self.player1_die4,"|",self.player1_die5, "|")
 
    

    


yahtzee1 = My_yahtzee("Tony")
yahtzee1.roll()