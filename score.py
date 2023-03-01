def score():
    print('Score() called from roll()')
    if player1_rollNumber == 1:
        print("How would you like to score your dice?: ") 
        player1_firstRoll[0]  = player1_die1
        player1_firstRoll[1] = player1_die2  
        player1_firstRoll[2] = player1_die3  
        player1_firstRoll[3] = player1_die4  
        player1_firstRoll[4] = player1_die5
        print("player1_first_roll: ", player1_firstRoll)
    
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

    player1_firstRollList = (player1_die1, player1_die2, player1_die3, player1_die4, player1_die5)
    print(player1_roll.player1_firstRollList)
    score_choice = input("Please choose one of the above options: ")
    if score_choice == "1" and my_yahtzee.player1_scorecard.player1_ones == None:
        player1_ones = player1_firstRollList.count(1)
        print("player1_ones", player1_ones)
        player1_scorecard()
    elif score_choice == "2":
        player1_twos = player1_firstRollList.count(2) * 2
        print("player1_twos", player1_twos)
    elif score_choice == "3":
        player1threes = player1_firstRollList.count(3) * 3
        print("player1_threes", player1_threes)
    elif score_choice == "4":
        player1_fours = player1_firstRollList.count(4) * 4
        print("player1_fours", player1_fours)
    elif score_choice == "5":
        player1_fives = player1_firstRollList.count(5) * 5
        print("player1_fives", player1_fives)
    elif score_choice =="6":
        player1_sixes = player1_firstRollList.count(6) * 6
        print("player1_sixes", player1_sixes)

    elif score_choice.upper() == "T":
        for i in player1_firstRollList:
            player1_3ofaKind == player1_3ofaKind + i
        print("You scored a 3o f a Kind: ", player1_3ofaKind)
    elif score_choice.upper() == "F":
        for i in player1_firstRollList:
            player1_4ofaKind == player1_4ofaKind + i
        print("You scored a 4 of a kind: ", player1_4ofaKind)
    elif score_choice.upper() == "FH":
        player1_fullHouse = 25
        print("You scored a Full House: ", player1_fullHouse)
    elif score_choice.upper() == "S":
        player1_SmallStraight = 30
        print("You scored Small Straight: ", player1_smallStraight)
    elif score_choice.upper() == "L":
        player1_LargeStraight = 40
        print("You scored a Large Straight: ", player1_largeStraight)
    elif score_choice.upper() == "S":
        player1_yahtzee = 50
        print("You scored a Yahtzee: ", player1_yahtzee)
    elif score_choice.upper() == "C":
        for i in player1_firstRollList:
            player1_chance = player1_chance + i   
        print("You scored a Chance: ", player1_chance)
    print('roll() called from score()')
    print("printing player1 scorecard")
        player1_scorecard()


