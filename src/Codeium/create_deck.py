import random

def create_deck():
    playData = {
        'player1_hand': [],
        'player2_hand': []
    }
    deck = []
    cards = ["14", "13", "12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02"]
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    for suit in suits:
        for card in cards:
            deck.append(card + suit)
    print("count:", len(deck))
    
    random.shuffle(deck)
    print("After shuffle 10 times:", deck)
    print("shuffled_deck:", deck)
    print("Type:", type(deck))
    
    for i, card in enumerate(deck):
        if i % 2 == 0:
            playData['player1_hand'].append(card)
        else:
            playData['player2_hand'].append(card)
    print("player1_hand_count:", len(playData['player1_hand']))
    print("player2_hand_count:", len(playData['player2_hand']))
    print("player1_hand:", playData['player1_hand'])
    print("player2_hand:", playData['player2_hand'])