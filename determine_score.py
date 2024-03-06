def bd_score(dice):
    # Count )the occurrences of each number in the bd_score
    print("dice type: ", type(dice))
    print(dice)
    counts = [dice.count(i) for i in range(1, 7)]
    
    # Check for Yahtzee (all dice are the same)
    if max(counts) == 5:
        return "Yahtzee!"
    
    # Check for Four of a Kind
    if max(counts) >= 4:
        return "Four of a Kind"
    
    # Check for Full House
    if 2 in counts and 3 in counts:
        return "Full House"
    
    # Check for Three of a Kind
    if max(counts) >= 3:
        return "Three of a Kind"
    
    # Check for Small Straight
    if counts == [1, 1, 1, 1, 0, 0] or counts == [0, 1, 1, 1, 1, 0] or counts == [0, 0, 1, 1, 1, 1] \
    or counts == [2, 1, 1, 1, 0, 0] or counts == [0, 2, 1, 1, 1, 0] or counts == [0, 0, 1, 2, 1, 1] \
    or counts == [1, 2, 1, 1, 0, 0] or counts == [0, 1, 2, 1, 1, 0] or counts == [0, 0, 2, 1, 1, 1] \
    or counts == [1, 1, 2, 1, 0, 0] or counts == [0, 1, 1, 2, 1, 0] or counts == [0, 0, 1, 1, 2, 1] \
    or counts == [1, 1, 1, 2, 0, 0] or counts == [0, 1, 1, 1, 2, 0] or counts == [0, 0, 1, 1, 1, 2]:
        return "Small Straight"
    
    # Check for Large Straight
    if counts == [0, 1, 1, 1, 1, 1] or counts == [1, 1, 1, 1, 1, 0]:
        return "Large Straight" 
    
    # If none of the above conditions are met, return "Chance"
    return "Chance"

dice = [1, 2, 3, 4, 5]
print(bd_score(dice))
dice = [1, 5, 5, 5, 5]
print(bd_score(dice))
dice = [1, 1, 2, 2, 2]
print(bd_score(dice))
dice = [3, 3, 3, 4, 5]
print(bd_score(dice))
dice = [5, 2, 3, 4, 5]
print(bd_score(dice))
dice = [1, 2, 3, 4, 5]


# score = bd_score(bd_score)
# print(f"The score for the bd_score {bd_score} is: {score}")
# '''
# In this program, the `yahtzee_score` function takes a list 
# of dice rolls as input and determines the corresponding Yahtzee 
# score. It uses a series of if statements to check for different scoring 
# combinations, starting from the highest-scoring combinations down to the 
# lowest-scoring ones. Finally, if none of the conditions are met, it returns 
# "Chance" as the score.

# You can test the program by providing a list of dice rolls and it will 
# output the corresponding Yahtzee score.
# '''