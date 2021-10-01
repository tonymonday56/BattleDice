# my_yahtzee.py
# initialize 5 dice for each player
import random
class My_yahtzee:
    def __init__(self, player_name):
        self.player_name = player_name

    def play(self):
        My_yahtzee.roll1()
        
        
    def roll1(self):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        discard1 = input("Would you like to discard die1? Y for Yes:")
        discard2 = input("Would you like to discard die2? Y for Yes:")
        discard3 = input("Would you like to discard die3? Y for Yes:")
        discard4 = input("Would you like to discard die4? Y for Yes:")
        discard5 = input("Would you like to discard die5? Y for Yes:")
        if discard1.upper() == "Y":
            die1 =random.randint(1,6)
        if discard2.upper() == "Y":
            die2 = random.randint(1,6)
        if discard3.upper == "Y":
            die3 = random.randint(1,6)
        if discard4.upper() == "Y":
            die4 = random.randint(1,6)
        if discard5.upper() == "Y":
            die5 = random.randint(1,6)


        print("Player Name: ", self.player_name)
        print(die1, die2, die3, die4, die5)
        return self.player_name, die1, die2, die3, die4, die5

    def roll2(self):
        pass
    
    def roll3(self):
        pass


yahtzee1 = My_yahtzee(1)
yahtzee1.roll1()