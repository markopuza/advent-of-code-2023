from common import library

CardGame = tuple[list[int]]

def parse_cards(card_desc: str) -> CardGame:
    winning_cards = list(map(int,card_desc.split(': ')[1].split(' | ')[0].split()))
    hand_cards = list(map(int,card_desc.split(': ')[1].split(' | ')[1].split()))
    return winning_cards, hand_cards

def count_scratchcards(cards: list[CardGame]) -> int:
    total = 0
    copies = [1] * len(cards)
    for i, (winning, hand) in enumerate(cards):
        total += copies[i]
        winning_cnt = sum(c in winning for c in hand)
        for j in range(winning_cnt):
            copies[i + j + 1] += copies[i]
    return total

def main():
    cards = [parse_cards(card_desc) for card_desc in library.read_input(4)]
    print(count_scratchcards(cards))

if __name__ == "__main__":
    main()