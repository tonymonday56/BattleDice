# score_turn.py
def score_turn(dice):
    # count the number of times each value appears in the dice roll
    count = [dice.count(i) for i in range(1, 7)]
    
    # calculate the score for each possible category
    ones = count[0] * 1
    twos = count[1] * 2
    threes = count[2] * 3
    fours = count[3] * 4
    fives = count[4] * 5
    sixes = count[5] * 6
    three_of_a_kind = sum(dice) if any(x >= 3 for x in count) else 0
    four_of_a_kind = sum(dice) if any(x >= 4 for x in count) else 0
    full_house = 25 if sorted(count) == [2, 3] else 0
    small_straight = 30 if [1, 2, 3, 4] == sorted([dice.count(i) for i in range(1, 5)]) else 0
    large_straight = 40 if [1, 2, 3, 4, 5] == sorted([dice.count(i) for i in range(1, 6)]) else 0
    yahtzee = 50 if 5 in count else 0
    chance = sum(dice)
    
    return [ones, twos, threes, fours, fives, sixes, three_of_a_kind, four_of_a_kind, full_house, small_straight, large_straight, yahtzee, chance]

# example usage
dice = [1, 2, 3, 4, 5]
print(score_turn(dice))
dice = [1, 2, 2, 4, 5]
print(score_turn(dice))
dice = [3, 3, 3, 4, 5]
print(score_turn(dice))
dice = [1, 1, 1, 1, 5]
print(score_turn(dice))
dice = [5, 2, 3, 4, 5]
print(score_turn(dice))
dice = [2, 2, 3, 3, 3]
print(score_turn(dice))
dice = [5, 5, 5, 5, 5]
print(score_turn(dice))

