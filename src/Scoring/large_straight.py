# large_straight.py

def large_straight(roll):
    roll_set = list(set(roll))
    print(roll_set)
    if len(roll_set) > 4:
        for i in roll_set:
            if roll_set[0] == 1 and roll_set[1] == 2 and roll_set[2] == 3 and roll_set[3] == 4 and roll_set[4] == 5:
                print("1large_straight")
                return "small_straight"
            elif roll_set[0] == 2 and roll_set[1] == 3 and roll_set[2] == 4 and roll_set[3] == 5 and roll_set[4] == 6: 
                print("2large_straight")
                return "large_straight"
            else:
                print(False)
                return False
    else:
        print(False)
        return False

roll = [1, 5, 4, 2, 3] #True
large_straight(roll)
roll = [6, 5, 4, 2, 3] #True
large_straight(roll)
roll = [1, 5, 4, 2, 3] #True
large_straight(roll)
roll = [2, 5, 4, 2, 3] #False
large_straight(roll)
roll = [2, 2, 4, 2, 3] #False
large_straight(roll)
roll = [6, 6, 4, 2, 3] #False
large_straight(roll)