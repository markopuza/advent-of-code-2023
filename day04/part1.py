from common import library

CardGame = tuple[list[int]]

def parse_cards(card_desc: str) -> CardGame:
    winning_cards = list(map(int,card_desc.split(': ')[1].split(' | ')[0].split()))
    hand_cards = list(map(int,card_desc.split(': ')[1].split(' | ')[1].split()))
    return winning_cards, hand_cards

def cards_value(cards: CardGame) -> int:
    winning, hand = cards
    winning_cnt = sum(c in winning for c in hand)
    return 0 if winning_cnt == 0 else 1 << (winning_cnt - 1)

def main():
    cards = [parse_cards(card_desc) for card_desc in library.read_input(4)]
    print(sum(cards_value(c) for c in cards))

if __name__ == "__main__":
    main()