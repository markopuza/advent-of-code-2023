from collections import Counter
from common import library

Hand = tuple[str]

CARDS = 'AKQJT98765432'
CARD_VALS = {
    c: i for i, c in enumerate(CARDS[::-1])
}

def parse_hands(hands_desc: list[str]) -> list[Hand]:
    return [r.split() for r in hands_desc]

def hand_valuator(hand: str) -> tuple[int]:
    c = Counter(hand)
    if 5 in c.values():
        total_hand_val = 7
    elif 4 in c.values():
        total_hand_val = 6
    elif 3 in c.values() and 2 in c.values(): 
        total_hand_val = 5
    elif 3 in c.values():
        total_hand_val = 4
    elif Counter(c.values())[2] == 2:
        total_hand_val = 3
    elif 2 in c.values():
        total_hand_val = 2
    else:
        total_hand_val = 1
    return tuple([total_hand_val] + [CARD_VALS[c] for c in hand])


def evaluate_hands(hands: list[Hand]) -> int:
    total = 0
    for rank, (hand, bid) in enumerate(sorted(hands, key=lambda x: hand_valuator(x[0])), 1):
        total += rank * int(bid)
    return total


def main():
    hands = parse_hands(library.read_input(7))
    print(evaluate_hands(hands))

if __name__ == "__main__":
    main()