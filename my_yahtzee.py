# my_yahtzee.py
# initialize 5 dice for each player
import random
class My_yahtzee:
    def __init__(self, player_num):
        self.player_num = player_num

    def roll(self):
        die1 = random.randint(1,6)
        print(self.player_num)
        print(die1)


yahtzee1 = My_yahtzee(1)
yahtzee1.roll()