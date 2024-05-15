# full_house.py

def full_house(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    dice_set = list(set(dice))
    print(dice_set)
    if len(dice_set) < 3:
        if 2 in counts and 3 in counts:
            print("Full House")
            return "Full House"
        else:
            print(False)
            return False
    else:
        print(False)
        return False

dice = [1, 1, 4, 4, 4] #True
full_house(dice)
dice = [6, 6, 6, 2, 2] #True
full_house(dice)
dice = [1, 5, 5, 1, 1] #True
full_house(dice)
dice = [2, 5, 4, 2, 3] #False
full_house(dice)
dice = [2, 2, 4, 2, 3] #False
full_house(dice)
dice = [6, 6, 4, 2, 3] #False
full_house(dice)
