# score.py
import bd as bd
import logging

def turn():
    pass

def score():

    print('Score() called from roll()')
    if bd.p1_roll.p1_rollNumber == 1:
        print("How would you like to score your dice?: ") 
        bd.p1_roll.p1_firstRollList[0] = bd.p1_roll.p1_die1
        bd.p1_roll.p1_firstRoll[1] = bd.p1_roll.p1_die2
        bd.p1_roll.p1_firstRoll[2] = bd.p1_roll.p1_die3
        bd.p1_roll.p1_firstRoll[3] = bd.p1_roll.p1_die4
        bd.p1_roll.p1_firstRoll[4] = bd.p1_roll.p1_die5
        print("p1_first_roll: ", bd.p1_roll.p1_firstRoll)

    print("Enter[1] to score Ones:")
    print("Enter[2] to score Twos: ")
    print("Enter[3] to score Threes: ")
    print("Enter[4] to score Fours: ")
    print("Enter[5] to score Fives: ")
    print("Enter[6] to score Sixes: ")
    print("Enter[T] to score a Three of a Kind: ")
    print("Enter[F] to score a Four of a Kind: ")
    print("Enter[FH] to score a Full House: ")
    print("Enter[S] to score a Small Stright House: ")
    print("Enter[L] to score a Large Straight: ")
    print("Enter[C] to score a Chance: ")
    print("Enter[Z] to score a Yahtzee: ")

    p1_firstRollList = (bd.p1_roll.p1_die1,
                        bd.p1_roll.p1_die2,
                        bd.p1_roll.p1_die3,
                        bd.p1_roll.p1_die4,
                        bd.p1_roll.p1_die5)

    print(bd.p1_roll.p1_firstRollList)
    score_choice = input("Please choose one of the above options: ")
    if score_choice == "1" and bd.p1_scorecard.p1_ones == 0:
        if score_choice == "1":
            p1_ones = p1_firstRollList.count(1)
            print("p1_ones", p1_ones)
            bd.p1_scorecard['p1_ones'] = p1_ones
            turn()
    elif score_choice == "2":
        if bd.p1_scorecard.p1_twos == 0:
            p1_twos = p1_firstRollList(2) * 2
            print("p1_twos", p1_twos)
            bd.p1_scorecard['p1_twos'] = p1_twos
            turn()
    elif score_choice == "3":
        if bd.p1_scorecard.p1_threes == None:
            p1_threes = p1_firstRollList.count(3) * 3
            print("p1_threes", p1_threes)
            bd.p1_scorecard['p1_threes'] = p1_threes
            turn()
    elif score_choice == "4":
        if bd.p1_scorecard.p1_fours == None:
            p1_fours = p1_firstRollList.count(4) * 4
            print("p1_fours", p1_fours)
            bd.p1_scorecard['p1_fours'] = p1_fours
            turn()
    elif score_choice == "5":
        if bd.p1_scorecard.p1_fives == None:
            p1_fives = p1_firstRollList.count(5) * 5
            print("p1_fives", p1_fives)
            bd.p1_scorecard['p1_fies'] = p1_fives
            turn()
    elif score_choice =="6":
        if bd.p1_scorecard.p1_sixes == None:
            p1_sixes = p1_firstRollList.count(6) * 6
            print("p1_sixes", p1_sixes)
            bd.p1_scorecard['p1_sixes'] = p1_sixes
            turn()
    elif score_choice.upper() == "T":
        if bd.p1_scorecard.p1_3ofaKind == None:
            for i in p1_firstRollList:
                bd.p1_scorecard.p1_3ofaKind == bd.p1_scorecard.p1_3ofaKind + i
                print("You scored a 3 of a Kind: ", bd.p1_scorecard.p1_3ofaKind)
                turn()
    elif score_choice.upper() == "F":
        if bd.p1_scorecard.p1_4ofaKind == None:
            for i in p1_firstRollList:
                bd.p1_scorecard.p1_4ofaKind == bd.p1_scorecard.p1_4ofaKind + i
                print("You scored a 4 of a kind: ", bd.p1_scorecard.p1_4ofaKind)
                turn()
    elif score_choice.upper() == "FH":
        if bd.p1_scorecard.p1_fullHouse == None:
            p1_fullHouse = 25
            print("You scored a Full House: ", bd.p1_scorecard.p1_fullHouse)
            turn()
    elif score_choice.upper() == "S":
        p1_SmallStraight = 30
        print("You scored Small Straight: ", bd.p1_scorecard.p1_smallStraight)
        turn()
    elif score_choice.upper() == "L":
        p1_LargeStraight = 40
        print("You scored a Large Straight: ", bd.p1_scorecard.p1_largeStraight)
        turn()
    elif score_choice.upper() == "S":
        p1_yahtzee = 50
        print("You scored a Yahtzee: ", bd.p1_scorecard.p1_yahtzee)
        turn()
    elif score_choice.upper() == "C":
        for i in p1_firstRollList:
            bd.p1_scorecard.p1_chance = bd.p1_scorecard.p1_chance + i   
        print("You scored a Chance: ", bd.p1_scorecard.p1_chance)
        turn()
    #TODO Implement turn() here so that the other player is current_player.

    print("printing p1 scorecard")
    bd.print_p1_scorecard()
    print('roll() called from score()')
    bd.roll()

