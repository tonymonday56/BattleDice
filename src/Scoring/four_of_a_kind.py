# four_of_a_kind.py

def four_of_a_kind(dice):
    counts = [dice.count(i) for i in range(1, 7)]
    dice_set = list(set(dice))
    print(dice_set)
    if len(dice_set) < 3:
        for count in counts:
            if 4 in counts:
                print("2four_of_a_kind")
                return "four_of_a_kind"
            elif 5 in counts:
                print("3four_of_a_kind")
                return "four_of_a_kind"
            else:
                print(False)
                return False
    else:
        print(False)
        return False
   
dice = [6, 1, 1, 1, 1] #True
four_of_a_kind(dice)
dice = [1, 1, 1, 1, 6] #True
four_of_a_kind(dice)
dice = [2, 2, 2, 2, 2] #True
four_of_a_kind(dice)
dice = [5, 5, 5, 6, 5] #True
four_of_a_kind(dice)
dice = [2, 5, 4, 2, 3] #False
four_of_a_kind(dice)
dice = [2, 4, 4, 2, 3] #False
four_of_a_kind(dice)
dice = [6, 6, 4, 2, 3] #False
four_of_a_kind(dice)

