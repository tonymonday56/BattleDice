# yahtzee.py

def yahtzee(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    dice_set = list(set(dice))
    print(dice_set)
    if len(dice_set) == 1:
        print("Yahtzee")
        return "Yahtzee"
    else:
        print(False)
        return False
   

dice = [1, 1, 1, 1, 1] #True
yahtzee(dice)
dice = [2, 2, 2, 2, 2] #True
yahtzee(dice)
dice = [5, 5, 5, 5, 5] #True
yahtzee(dice)
dice = [2, 5, 4, 2, 3] #False
yahtzee(dice)
dice = [2, 2, 4, 2, 3] #False
yahtzee(dice)
dice = [6, 6, 4, 2, 3] #False
yahtzee(dice)
