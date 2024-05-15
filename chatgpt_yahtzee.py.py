import random

class YahtzeeGame:
    def __init__(self):
        self.scorecard = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Yahtzee": None,
            "Chance": None
        }
        self.roll = [0, 0, 0, 0, 0]
        self.rolls_left = 3

    def roll_dice(self, keep=None):
        if keep is None:
            self.roll = [random.randint(1, 6) for _ in range(5)]
        else:
            for i in range(5):
                if keep[i] == 0:
                    self.roll[i] = random.randint(1, 6)
        self.rolls_left -= 1
        return self.roll

    def display_roll(self):
        print("Current Roll:", self.roll)

    def display_scorecard(self):
        print("\nScorecard:")
        for category, score in self.scorecard.items():
            if score is None:
                print(f"{category}:")
            else:
                print(f"{category}: {score}")
        print()

    def update_scorecard(self, category):
        if self.scorecard[category] is not None:
            print("You've already scored that category. Please choose another.")
            return False
        else:
            score = self.calculate_score(category)
            self.scorecard[category] = score
            print(f"Scored {score} points for {category}!")
            return True

    def calculate_score(self, category):
        # Implement the scoring logic for each category
        if category in ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"):
            return self.roll.count(int(category[0])) * int(category[0])
        elif category == "Three of a Kind":
            for num in self.roll:
                if self.roll.count(num) >= 3:
                    return sum(self.roll)
            return 0
        elif category == "Four of a Kind":
            for num in self.roll:
                if self.roll.count(num) >= 4:
                    return sum(self.roll)
            return 0
        elif category == "Full House":
            counts = [self.roll.count(num) for num in set(self.roll)]
            if 2 in counts and 3 in counts:
                return 25
            return 0
        elif category == "Small Straight":
            if len(set(self.roll)) >= 4:
                sorted_roll = sorted(set(self.roll))
                if sorted_roll in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
                    return 30
            return 0
        elif category == "Large Straight":
            if len(set(self.roll)) == 5:
                sorted_roll = sorted(set(self.roll))
                if [1, 2, 3, 4, 5] == sorted_roll or [2, 3, 4, 5, 6] == sorted_roll:
                    return 40
            return 0
        elif category == "Yahtzee":
            if len(set(self.roll)) == 1:
                return 50
            return 0
        elif category == "Chance":
            return sum(self.roll)
        else:
            return "Invalid category"

    def play_game(self):
        print("Welcome to Yahtzee!")
        while any(score is None for score in self.scorecard.values()):
            print("\nNew Turn!")
            self.rolls_left = 3
            self.roll_dice()
            while self.rolls_left > 0:
                self.display_roll()
                print("Rolls left:", self.rolls_left)
                choice = input("Enter dice indexes to keep (e.g., '135') or 'r' to re-roll all: ")
                if choice.lower() == 'r':
                    self.roll_dice()
                else:
                    keep = [0] * 5
                    for index in choice:
                        keep[int(index) - 1] = 1
                    self.roll_dice(keep)
                self.display_roll()

                if self.rolls_left > 0:
                    category = input("Enter category to score this roll: ")
                    if category in self.scorecard:
                        if self.update_scorecard(category):
                            break
                    else:
                        print("Invalid category. Please choose from the scorecard.")

        print("\nGame Over!")
        print("Final Scorecard:")
        self.display_scorecard()
        print("Total Score:", sum(filter(None, self.scorecard.values())))


# Start the game
yahtzee = YahtzeeGame()
yahtzee.play_game()
