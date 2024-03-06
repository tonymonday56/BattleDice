def check_large_straight(dice_values):
    """
    Given a list of dice values, checks if it represents a large straight in the game of dice.
    
    Parameters:
        dice_values (list): A list of integers representing the values of the dice.
        
    Returns:
        tuple: A tuple containing a boolean indicating if the list represents a large straight,
               and an integer representing the roll value.
    """
    roll_value = 0
    dice_values.sort()
    if dice_values == [1, 2, 3, 4, 5] or dice_values == [2, 3, 4, 5, 6]:
        roll_value = 40
        return True, roll_value
    else:
        return False, roll_value