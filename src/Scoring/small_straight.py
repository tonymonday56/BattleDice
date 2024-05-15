# small_straight.py

def small_straight(roll):
    roll_set = list(set(roll))
    print(roll_set)
    if len(roll_set) > 3:
        for i in roll_set:
            if roll_set[0] == 1 and roll_set[1] == 2 and roll_set[2] == 3 and roll_set[3] == 4:
                print("1small_straight")
                return "small_straight"
            elif roll_set[0] == 2 and roll_set[1] == 3 and roll_set[2] == 4 and roll_set[3] == 5: 
                print("2small_straight")
                return "small_straight"
            elif roll_set[0] == 3 and roll_set[1] == 4 and roll_set[2] == 5 and roll_set[3] == 6:
                print("4small_straight")
                return "small_straight"
            elif roll_set[1] == 3 and roll_set[2] == 4 and roll_set[3] == 5 and roll_set[4] == 6:
                print("5small_straight")
                return "small_straight"
            elif roll_set[2] == 3 and roll_set[3] == 4 and roll_set[4] == 5 and roll[5] == 6:
                print("6small_straight")
                return "small_straight"
            else:
                print(False)
                return False
    else:
        print(False)
        return False
    
roll = [1, 2, 3, 3, 4] #True
small_straight(roll)
roll = [1, 2, 3, 4, 5] #True
small_straight(roll)
roll = [3, 5, 6, 1, 4] #True
small_straight(roll)
roll = [1, 5, 3, 4, 6] #True
small_straight(roll)
roll = [4, 5, 2, 3, 5] #True
small_straight(roll)
roll = [1, 4, 3, 2, 2] #True
small_straight(roll)
roll = [5, 4, 3, 6, 3] #True
small_straight(roll)
roll = [5, 3, 5, 4, 6] #True
small_straight(roll)
roll = [2, 4, 5, 1, 3] #True
small_straight(roll)
roll = [3, 6, 4, 5, 3] #True
small_straight(roll)
roll = [5, 6, 4, 3, 5] #True
small_straight(roll)
roll = [4, 5, 3, 6, 3] #True
small_straight(roll)
roll = [4, 5, 5, 3, 2] #True
small_straight(roll)
roll = [4, 5, 2, 3, 5] #True
small_straight(roll)
roll = [4, 6, 5, 3, 6] #True
small_straight(roll)
roll = [4, 2, 3, 1, 5] #True
small_straight(roll)
roll = [3, 6, 4, 6, 5] #True
small_straight(roll)
roll = [5, 2, 1, 3, 4] #True
small_straight(roll)
roll = [4, 4, 1, 2, 3] #True
small_straight(roll)
roll = [4, 1, 4, 2, 3] #True
small_straight(roll)
roll = [5, 1, 4, 3, 6] #True
small_straight(roll)
roll = [5, 2, 2, 3, 4] #True
small_straight(roll)
roll = [4, 4, 6, 5, 3] #True
small_straight(roll)
roll = [2, 4, 3, 5, 1] #True
small_straight(roll)
roll = [5, 4, 2, 5, 3] #True
small_straight(roll)
roll = [2, 3, 5, 5, 4] #True
small_straight(roll)
roll = [1, 6, 3, 4, 5] #True
small_straight(roll)
roll = [4, 5, 3, 3, 6] #True
small_straight(roll)
roll = [6, 4, 3, 6, 5] #True
small_straight(roll)
roll = [4, 6, 6, 5, 3] #True
small_straight(roll)
roll = [4, 3, 5, 2, 2] #True
small_straight(roll)
roll = [2, 3, 2, 1, 4] #True
small_straight(roll)
roll = [4, 2, 6, 1, 3] #True
small_straight(roll)
roll = [4, 4, 5, 3, 6] #True
small_straight(roll)
roll = [4, 5, 6, 3, 6] #True
small_straight(roll)
roll = [1, 2, 3, 5, 6] # False
small_straight(roll)
roll = [5, 1, 1, 6, 6] # False
small_straight(roll)
roll = [4, 6, 4, 1, 1] # False
small_straight(roll)
roll = [6, 4, 1, 6, 4] # False
small_straight(roll)
roll = [4, 6, 3, 6, 6] # False
small_straight(roll)
roll = [2, 1, 4, 6, 4] # False
small_straight(roll)
roll = [2, 6, 1, 5, 6] # False
small_straight(roll)
roll = [2, 6, 1, 5, 6] # False
small_straight(roll)
roll = [3, 6, 5, 3, 2] # False
small_straight(roll)
roll = [3, 2, 3, 5, 3] # False
small_straight(roll)
roll = [5, 5, 6, 2, 3] # False
small_straight(roll)
roll = [3, 4, 6, 4, 3] # False
small_straight(roll)
roll = [1, 4, 5, 5, 1] # False
small_straight(roll)
roll = [1, 4, 4, 4, 1] # False
small_straight(roll)
roll = [1, 6, 5, 1, 4] # False
small_straight(roll)
roll = [6, 6, 4, 5, 4] # False
small_straight(roll)
roll = [5, 3, 3, 3, 2] # False
small_straight(roll)
roll = [5, 2, 1, 5, 3] # False
small_straight(roll)
roll = [3, 5, 1, 6, 2] # False
small_straight(roll)
roll = [6, 4, 2, 1, 2] # False
small_straight(roll)
roll = [1, 3, 1, 3, 2] # False
small_straight(roll)
roll = [3, 1, 3, 4, 3] # False
small_straight(roll)
roll = [4, 3, 1, 6, 3] # False
small_straight(roll)
roll = [4, 6, 3, 3, 6] # False
small_straight(roll)
roll = [3, 6, 3, 6, 4] # False
small_straight(roll)
roll = [1, 1, 3, 1, 3] # False
small_straight(roll)
roll = [5, 5, 1, 3, 2] # False
small_straight(roll)
roll = [3, 4, 2, 6, 6] # False
small_straight(roll)
roll = [5, 4, 2, 6, 1] # False
small_straight(roll)
roll = [2, 4, 4, 5, 4] # False
small_straight(roll)
roll = [3, 6, 2, 5, 5] # False
small_straight(roll)
roll = [2, 5, 3, 5, 1] # False
small_straight(roll)
roll = [3, 2, 2, 3, 4] # False
small_straight(roll)
roll = [5, 2, 2, 6, 2] # False
small_straight(roll)
roll = [5, 6, 2, 5, 6] # False
small_straight(roll)
