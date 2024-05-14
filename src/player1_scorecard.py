# player1_scorecard.py
def player1_scorecard(self):
    p1_scores = {
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "3Kind": None,
        "4Kind": None,
        "FullHouse": None,
        "SmallStraight": None,
        "LargeStraight": None,
        "Yahtzee": None,
        "Chance": None
    }
cur_score = 0

SCORE_METHODS = {
        "1": (lambda hand: hand.get_counts()[0] * 1),
        "2": (lambda hand: hand.get_counts()[1] * 2),
        "3": (lambda hand: hand.get_counts()[2] * 3),
        "4": (lambda hand: hand.get_counts()[3] * 4),
        "5": (lambda hand: hand.get_counts()[4] * 5),
        "6": (lambda hand: hand.get_counts()[5] * 6),
        "3Kind": (lambda hand: hand.get_hand_total_score() if hand.is_triple() else 0),
        "4Kind": (lambda hand: hand.get_hand_total_score() if hand.is_four_of_a_kind() else 0),
        "FullHouse": (lambda hand: 25 if hand.is_full_house() else 0),
        "SmallStraight": (lambda hand: 30 if hand.is_small_straight() else 0),
        "LargeStraight": (lambda hand: 40 if hand.is_large_straight() else 0),
        "Yahtzee": (lambda hand: 50 if hand.is_yahtzee() else 0),
        "Chance": (lambda hand: hand.get_hand_total_score()),
    }
        
        