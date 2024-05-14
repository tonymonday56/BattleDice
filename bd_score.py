# bd_score.py
pl_score = {}
def battleDice_score(dice):
    scoring_list = []
    # Count the occurrences of each number in the roll
    counts = [dice.count(i) for i in range(1, 7)]
    
    # Check for Yahtzee (all dice are the same)
    if max(counts) == 5:
        # Die equals 5 of a kind.  EX: 5 5 5 5 5
        # Append to scoring_list for customer scoring option
        scoring_list.append("Bunker Buster | Yahtzee")
        return "Bunker Buster / Yahtzee!"
    
    # Check for Four of a Kind
    if max(counts) >= 4:
         # Die equals or is greater than 4 of a kind.  EX: 5 5 5 5 6
        # Append to scoring_list for customer scoring option
        scoring_list.append("Four of a Kind")
        return "Four of a Kind"
    
    # Check for Full House
    if 2 in counts and 3 in counts:
         # Die equals 5 of a kind and remaing die are tge same.  EX: 5 5 2 2 2
        # Append to scoring_list for customer scoring option
        scoring_list.append("Full House")
        return "Full House"
    
    # Check for Three of a Kind
    if max(counts) >= 3: # Die equals 5 of a kind.  EX: 5 5 5 5 5
        # Append to scoring_list for customer scoring option
        scoring_list.append("Three of a Kind")
        return "Three of a Kind"
    
    # Check for Small Straight
    if counts == [1, 1, 1, 1, 0, 0] or counts == [0, 1, 1, 1, 1, 0] or counts == [0, 0, 1, 1, 1, 1] \
    or counts == [2, 1, 1, 1, 0, 0] or counts == [0, 2, 1, 1, 1, 0] or counts == [0, 0, 1, 2, 1, 1] \
    or counts == [1, 2, 1, 1, 0, 0] or counts == [0, 1, 2, 1, 1, 0] or counts == [0, 0, 2, 1, 1, 1] \
    or counts == [1, 1, 2, 1, 0, 0] or counts == [0, 1, 1, 2, 1, 0] or counts == [0, 0, 1, 1, 2, 1] \
    or counts == [1, 1, 1, 2, 0, 0] or counts == [0, 1, 1, 1, 2, 0] or counts == [0, 0, 1, 1, 1, 2]:
        scoring_list.append("Small Straight")
        return "Small Straight"
        
    
    # Check for Large Straight
    if counts == [0, 1, 1, 1, 1, 1, 1] or  counts == [ 1, 1, 1, 1, 1, 0]:
        scoring_list.append("Large Straight")
        return "Large Straight"
    
    # scoring_list.append("Chance") always add to scoring_list.  
    # scorecard parser will clean out the remaining options
    scoring_list.append("Chance")


print("Scoring_List:\n")
print(scoring_list)


# Example usage
#roll = [1, 2, 3, 4, 5]
#roll = [1, 2, 3, 4, 5]
#roll = [2, 2, 2, 4, 5]
#roll = [2, 2, 2, 4, 4]
roll = [2, 2, 2, 2, 5]
#roll = [2, 2, 2, 2, 2]

score = battleDice_score(roll)
print(f"The score for the roll {roll} is: {score}")
