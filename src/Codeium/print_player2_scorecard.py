#file: print_player2_scorecard.py
def print_player2_scorecard():
    """
    Print the scorecard for player 2.

    This function prints out the scores for each category on the scorecard
    for player 2.

    Args:
        None

    Returns:
        None
    """
    print("Ones: ", player2_scorecard.get('player2_ones'))  # Print the score for ones category
    print("Twos: ", player2_scorecard.get('player2_twos'))  # Print the score for twos category
    print("Threes: ", player2_scorecard.get('player2_threes'))  # Print the score for threes category
    print("Fours: ", player2_scorecard.get('player2_fours'))  # Print the score for fours category
    print("Fives: ", player2_scorecard.get('player2_fives'))  # Print the score for fives category
    print("Sixes: ", player2_scorecard.get('player2_sixes'))  # Print the score for sixes category
    print("Upper Total: ", player2_scorecard.get('player2_upperAmount'))  # Print the upper total score
    print("Upper Bonus:", player2_scorecard.get('player2_upperBonus'))  # Print the upper bonus score
    print("Upper Total: ", player2_scorecard.get('player2_upperTotal'))  # Print the upper total score
    print("3 of a Kind: ", player2_scorecard.get('player2_3ofaKind'))  # Print the score for three of a kind category
    print("4 of a Kind: ", player2_scorecard.get('player2_4ofaKind'))  # Print the score for four of a kind category
    print("Full House: ", player2_scorecard.get('player2_fullHouse'))  # Print the score for full house category
    print("Small Straight: ", player2_scorecard.get('player2_smallStraight'))  # Print the score for small straight category
    print("Large Straight: ", player2_scorecard.get('player2_largeStraight'))  # Print the score for large straight category
    print("Yahtzee: ", player2_scorecard.get('player2_yahtzee'))  # Print the score for yahtzee category
    print("Chance: ", player2_scorecard.get('player2_chance'))  # Print the score for chance category
    print("Lower Total: ", player2_scorecard.get('player2_lowerTotal'))  # Print the lower total score
    print("Total: ", player2_scorecard.get('player2_total'))  # Print the total score