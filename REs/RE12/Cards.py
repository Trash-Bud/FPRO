import random
from typing import List, Tuple
def card_value(card):
    if card[1] == "J" or card[1] == "Q" or card[1] == "K":
        value = 10
    elif card[1] == "A":
        value = 11
    else:
        value = int(card[1])
    if card[0] == "♠" or card[0] == "♣":
        return value*2
    return value

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(seed, shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    global drng
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        drng.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items, seed):
    """Choose and return a random item"""
    global drng
    return drng.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def play(seed):
    """Play a 4-player card game"""
    global drng
    drng = random.Random(seed)
    deck = create_deck(seed, shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names, seed)
    turn_order = player_order(names, start=start_player)
    turn_wins = {"P1": 0, "P2": 0, "P3": 0, "P4": 0}
    while hands[start_player]:
        turn = []
        for name in turn_order:
            card = choose(hands[name], seed)
            turn.append(card_value(card))
            hands[name].remove(card)
        winner = max(turn)
        for i in range(len(turn)):
            if winner == turn[i]:
                turn_wins[turn_order[i]] += 1
    winner_turnc = max(turn_wins.values())
    result = ""
    for i in turn_wins:
        if turn_wins[i] == winner_turnc:
            if result == "":
                result += i
            else:
                result += " " + i
    return result

print(play(580))