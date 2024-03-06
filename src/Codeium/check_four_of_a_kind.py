#file: check_four_of_a_kind.py
def check_four_of_a_kind(die_list):
    """
    Check if the given list of dice values contains four of a kind.

    Parameters:
    - die_list (list): A list of integers representing the values of the dice.

    Returns:
    - tuple: A tuple containing a boolean indicating if four of a kind was found
             and the sum of the dice values.
    """
    roll_value = sum(die_list)
    if die_list[0] == die_list[3] or die_list[1] == die_list[4]:
        return True, roll_value
    return False, roll_value