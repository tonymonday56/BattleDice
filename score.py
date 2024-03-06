# score.py
import BattleDice
import logging
def turn():
    pass
def score():
    print('Score() called from roll()')
    if BattleDice.player1_roll.player1_rollNumber == 1:
        print("How would you like to score your dice?: ") 
        BattleDice.player1_roll.player1_firstRoll[0] = BattleDice.player1_roll.player1_die1
        BattleDice.player1_roll.player1_firstRoll[1] = BattleDice.player1_roll.player1_die2  
        BattleDice.player1_roll.player1_firstRoll[2] = BattleDice.player1_roll.player1_die3  
        BattleDice.player1_roll.player1_firstRoll[3] = BattleDice.player1_roll.player1_die4  
        BattleDice.player1_roll.player1_firstRoll[4] = BattleDice.player1_roll.player1_die5
        print("player1_first_roll: ", BattleDice.player1_roll.player1_firstRoll)
    
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

    player1_firstRollList = (BattleDice.player1_roll.player1_die1, 
                             BattleDice.player1_roll.player1_die2, 
                             BattleDice.player1_roll.player1_die3, 
                             BattleDice.player1_roll.player1_die4, 
                             BattleDice.player1_roll.player1_die5)
    print(BattleDice.player1_roll.player1_firstRollList)
    score_choice = input("Please choose one of the above options: ")
    if score_choice == "1" and BattleDice.player1_scorecard.player1_ones == None:
        if score_choice == "1":
            player1_ones = player1_firstRollList.count(1)
            print("player1_ones", player1_ones)
            BattleDice.player1_scorecard['player1_ones'] = player1_ones
            turn()
    elif score_choice == "2":
        if BattleDice.player1_scorecard.player1_twos == None:
            player1_twos = player1_firstRollList.count(2) * 2
            print("player1_twos", player1_twos)
            BattleDice.player1_scorecard['player1_twos'] = player1_twos
            turn()
    elif score_choice == "3":
        if BattleDice.player1_scorecard.player1_threes == None:
            player1_threes = player1_firstRollList.count(3) * 3
            print("player1_threes", player1_threes)
            BattleDice.player1_scorecard['player1_threes'] = player1_threes
            turn()
    elif score_choice == "4":
        if BattleDice.player1_scorecard.player1_fours == None:
            player1_fours = player1_firstRollList.count(4) * 4
            print("player1_fours", player1_fours)
            BattleDice.player1_scorecard['player1_fours'] = player1_fours
            turn()
    elif score_choice == "5":
        if BattleDice.player1_scorecard.player1_fives == None:
            player1_fives = player1_firstRollList.count(5) * 5
            print("player1_fives", player1_fives)
            BattleDice.player1_scorecard['player1_fies'] = player1_fives
            turn()
    elif score_choice =="6":
        if BattleDice.player1_scorecard.player1_sixes == None:
            player1_sixes = player1_firstRollList.count(6) * 6
            print("player1_sixes", player1_sixes)
            BattleDice.player1_scorecard['player1_sixes'] = player1_sixes
            turn()
    elif score_choice.upper() == "T":
        if BattleDice.player1_scorecard.player1_3ofaKind == None:
            for i in player1_firstRollList:
                BattleDice.player1_scorecard.player1_3ofaKind == BattleDice.player1_scorecard.player1_3ofaKind + i
                print("You scored a 3 of a Kind: ", BattleDice.player1_scorecard.player1_3ofaKind)
                turn()
    elif score_choice.upper() == "F":
        if BattleDice.player1_scorecard.player1_4ofaKind == None:
            for i in player1_firstRollList:
                BattleDice.player1_scorecard.player1_4ofaKind == BattleDice.player1_scorecard.player1_4ofaKind + i
                print("You scored a 4 of a kind: ", BattleDice.player1_scorecard.player1_4ofaKind)
                turn()
    elif score_choice.upper() == "FH":
        if BattleDice.player1_scorecard.player1_fullHouse == None:
            player1_fullHouse = 25
            print("You scored a Full House: ", BattleDice.player1_scorecard.player1_fullHouse)
            turn()
    elif score_choice.upper() == "S":
        player1_SmallStraight = 30
        print("You scored Small Straight: ", BattleDice.player1_scorecard.player1_smallStraight)
        turn()
    elif score_choice.upper() == "L":
        player1_LargeStraight = 40
        print("You scored a Large Straight: ", BattleDice.player1_scorecard.player1_largeStraight)
        turn()
    elif score_choice.upper() == "S":
        player1_yahtzee = 50
        print("You scored a Yahtzee: ", BattleDice.player1_scorecard.player1_yahtzee)
        turn()
    elif score_choice.upper() == "C":
        for i in player1_firstRollList:
            BattleDice.player1_scorecard.player1_chance = BattleDice.player1_scorecard.player1_chance + i   
        print("You scored a Chance: ", BattleDice.player1_scorecard.player1_chance)
        turn()
    #TODO Implement turn() here so that the other player is current_player.

    print("printing player1 scorecard")
    BattleDice.print_player1_scorecard()
    print('roll() called from score()')
    BattleDice.roll()

