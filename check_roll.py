# check_roll.py

def check_yahtzee(die_list):  # list of 5 die
    """
	Check if all the dice in the given list have the same value.

	Parameters:
	- die_list (list): A list of 5 die values.

	Returns:
	- True, 50: If all the dice have the same value, returns True and the value 50.
	- False, 0: If the dice do not have the same value, returns False and the value 0.
	"""
    roll_value = 0
    if len(set(die_list)) == 1:
        roll_value = 50
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value
print("Test check_yahtzee")
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

print("Test check_fullHouse")
print("check_fullHouse")
check_fullHouse([2, 3, 3, 5, 2])
check_fullHouse([2, 3, 3, 2, 2])


def check_largeStraight(die_list):
    """
    Given a list of dice values, checks if it represents a large straight in the game of dice.
    
    Parameters:
        die_list (list): A list of integers representing the values of the dice.
        
    Returns:
        tuple: A tuple containing a boolean indicating if the list represents a large straight,
               and an integer representing the roll value.
    """
    roll_value = 0
    die_list.sort()
    die_list_set = set(die_list)
    die_list2 = list(die_list_set)
    if die_list2 == [1,2,3,4,5] or die_list2 == [2,3,4,5,6] or die_list2 == [1,2,3,4,5,6]:    
        roll_value = 40
        print(True, roll_value)
        return True, roll_value
    else:
        print(False, roll_value)
        return False, roll_value

print("Test check_largeStraight")
print("check_largeStraight")
check_largeStraight([1,2,3,4,5]) # -->True
check_largeStraight([1,1,3,4,5]) # -->False
check_largeStraight([1,2,3,4,6]) # -->False
check_largeStraight([2,3,4,5,6]) # -->True



def check_smallStraight(die_list):
    """
    Checks if the given list of dice values forms a small straight.

    Parameters:
    die_list (list[int]): A list of integers representing the values of dice rolled.

    Returns:
    bool: True if the list forms a small straight, False otherwise.
    int: The roll value, which is always 30 if the list forms a small straight, or 0 otherwise.
    """
    roll_value = 0
    die_list.sort()
    die_list_set = set(die_list)
    die_list2 = list(die_list_set)
    #  
    if die_list2[0] == 1 and die_list2[1] == 2 and die_list2[2] == 3 and die_list2[3] == 4:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[0] == 2 and die_list2[1] == 3 and die_list2[2] == 4 and die_list2[3] == 5:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[0] == 3 and die_list2[1] == 4 and die_list2[2] == 5 and die_list2[3] == 6:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[1] == 1 and die_list2[2] == 2 and die_list2[3] == 3 and die_list2[4] == 4:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[1] == 2 and die_list2[2] == 3 and die_list2[3] == 4 and die_list2[4] == 5:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[1] == 3 and die_list2[2] == 4 and die_list2[3] == 5 and die_list2[4] == 6:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[2] == 1 and die_list2[3] == 2 and die_list2[4] == 3 and die_list2[5] == 4:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[2] == 2 and die_list2[3] == 3 and die_list2[4] == 4 and die_list2[5]== 5:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    elif die_list2[2] == 3 and die_list2[3] == 4 and die_list2[4] == 5 and die_list2[5] == 6:
        roll_value = 30
        print(True, roll_value)
        return True, roll_value
    else:
        print(False, roll_value)
        return False, roll_value
    

print("Test check_smallStraight")
print("check_smallStraight")
check_smallStraight([1, 2, 3, 4, 4])
check_smallStraight([5, 2, 3, 4, 4])
check_smallStraight([6, 2, 3, 4, 4])

def check_4ofaKind(die_list):
    """
    Check if the given list of dice values contains four of a kind.

    Parameters:
    - die_list (list): A list of integers representing the values of the dice.

    Returns:
    - tuple: A tuple containing a boolean indicating if four of a kind was found
     and the sum of the dice values.
    """
    roll_value = 0
    die_list.sort()
    if die_list[0] == die_list[3] or die_list[1] ==  die_list[4]:
        roll_value = sum(die_list)
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print("Test check_4ofaKind")
print("check_4ofaKind")
check_4ofaKind([1, 2, 2, 2, 2])
check_4ofaKind([1, 1, 2, 2, 2])

def check_3ofaKind(die_list):
    """
    Check if the given list of dice values contains three of a kind.

    Parameters:
    - die_list (list): A list of integers representing the values of the dice.

    Returns:
    - tuple: A tuple containing a boolean indicating if three of a kind was found
             and the sum of the dice values.
    """
    roll_value = 0
    die_list.sort()
    if die_list[0] == die_list[2] or die_list[1] == die_list[4] or die_list[2] == die_list[4]:
        roll_value = sum(die_list)
        print(True, roll_value)
        return True, roll_value
    print(False, roll_value)
    return False, roll_value

print("Test check_3ofaKind")
print("check_3ofaKind")
check_3ofaKind([1, 2, 3, 3, 3])
check_3ofaKind([1, 1, 1, 3, 3])
check_3ofaKind([1, 2, 3, 3, 4])

