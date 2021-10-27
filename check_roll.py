# check_roll.py

def check_yahtzee(die_list):  # list of 5 die
    roll_value = 0
    if len(set(die_list)) == 1:
        roll_value = 50
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print()
print("check_yahtzee")
check_yahtzee([1, 2, 3, 2, 1])
check_yahtzee([1, 1, 1, 1, 1])

def check_fullHouse(die_list):
    roll_value = 0
    die_list.sort()
    # check to see if there are any sets of 2 due that match.
    if (len(set(die_list))) != 2:
        print(False, roll_value)
        return False, roll_value
    elif die_list[0] != die_list[3] or die_list[1] != die_list[4]:
        roll_value = 25
    print(True, roll_value)
    return True, roll_value

print()
print("check_fullHouse")
check_fullHouse([2, 3, 3, 5, 2])
check_fullHouse([2, 3, 3, 2, 2])


def check_largeStraight(die_list):
    roll_value = 0
    die_list.sort()
    if len(set(die_list)) == 5:
        roll_value = 40
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print()
print("check_largeStraight")
check_largeStraight([1,2,3,4,5])
check_largeStraight([1,1,3,4,5])


def check_smallStraight(die_list):
    roll_value = 0
    die_list.sort()
    die_list_set = set(die_list)
    #  
    if len(die_list_set) == 4 and (die_list_set[0] + 3) == die_list_set[3]:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif len(die_list_set) == 4 and (die_list_set[1] + 3) == die_list_set[4]:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif len(die_list_set) == 4 and (die_list_set[2] + 3) == die_list_set[5]:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print()
print("check_smallStraight")
check_smallStraight([1, 2, 3, 4, 4])
check_smallStraight([5, 2, 3, 4, 4])

def check_4ofaKind(die_list):
    roll_value = 0
    die_list.sort()
    if die_list[0] == die_list[3] or die_list[1] ==  die_list[4]:
        roll_value = sum(die_list)
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print()
print("check_4ofaKind")
check_4ofaKind([1, 2, 2, 2, 2])
check_4ofaKind([1, 1, 2, 2, 2])

def check_3ofaKind(die_list):
    roll_value = 0
    die_list.sort()
    if die_list[0] == die_list[2] or die_list[1] == die_list[4] or die_list[2] == die_list[4]:
        roll_value = sum(die_list)
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print()
print("check_3ofaKind")
check_3ofaKind([1, 2, 3, 3, 3])
check_3ofaKind([1, 1, 1, 3, 3])
check_3ofaKind([1, 2, 3, 3, 4])





