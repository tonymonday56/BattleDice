# my_yahtzee.py
# initialize 5 dice for each player
import random
class My_yahtzee:
    die1 = 0
    die2 = 0
    die3 = 0
    die4 = 0
    die5 = 0
    def __init__(self, player_name):
        self.player_name = player_name

    def play(self):
        My_yahtzee.roll1()
        My_yahtzee.roll2()
        My_yahtzee.roll3()
        
        
    def roll1(self):
        '''Initial roll of the dice'''
        My_yahtzee.die1 = random.randint(1,6)
        My_yahtzee.die2 = random.randint(1,6)
        My_yahtzee.die3 = random.randint(1,6)
        My_yahtzee.die4 = random.randint(1,6)
        My_yahtzee.die5 = random.randint(1,6)
        print("Hand for", self.player_name, "after initial roll.")
        print(self.player_name, "Your hand: ", My_yahtzee.die1, My_yahtzee.die2, My_yahtzee.die3, My_yahtzee.die4, My_yahtzee.die5)


        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        if discard1.upper() == "Y":
            My_yahtzee.die1 =random.randint(1,6)
        if discard2.upper() == "Y":
            My_yahtzee.die2 = random.randint(1,6)
        if discard3.upper == "Y":
            My_yahtzee.die3 = random.randint(1,6)
        if discard4.upper() == "Y":
            My_yahtzee.die4 = random.randint(1,6)
        if discard5.upper() == "Y":
            My_yahtzee.die5 = random.randint(1,6)


        print("Player Name: ", self.player_name)
        print("This is your current hand after 2nd roll")
        print(self.player_name, "Your hand: ", My_yahtzee.die1, My_yahtzee.die2, My_yahtzee.die3, My_yahtzee.die4, My_yahtzee.die5)
        return self.player_name, My_yahtzee.die1, My_yahtzee.die2, My_yahtzee.die3, My_yahtzee.die4, My_yahtzee.die5

    def score(self):
        how_to_score = input("How would you like to score your dice?") 
        upper_card1 = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0}
        print("1 for Ones")
        print("2 for Twos")
        print("3 for Threes")
        print("4 for Fours")
        print("5 for Fives")
        print("6 for Sixes")

        score_choice_upper1 = input("Please choose one of the above options:")
        if score_choice_upper1 == 1:
            upper_card1["Ones"] = 
    def roll2(self):
        pass
    
    def roll3(self):
        pass


yahtzee1 = My_yahtzee("Tony")
yahtzee1.roll1()