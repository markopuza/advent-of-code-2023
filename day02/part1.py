from common import library

def parse_game(game_desc: str) -> list[tuple[int]]:
    res = []
    for s in game_desc.split(': ')[-1].split('; '):
        r, g, b = 0, 0, 0
        for item in s.split(', '):
            match item.strip().split(' '):
                case (cnt, "red"):
                    r += int(cnt)
                case (cnt, "green"):
                    g += int(cnt)
                case (cnt, "blue"):
                    b += int(cnt)
        res.append((r, g, b))
    return res

def game_possible_with(game_desc: str, r_lim: int, g_lim: int, b_lim: int) -> bool:
    for r, g, b in parse_game(game_desc):
        if not (r <= r_lim and g <= g_lim and b <= b_lim):
            return False
    return True

def main():
    result = 0
    games = library.read_input(2)
    for i, g in enumerate(games, 1):
        if game_possible_with(g, 12, 13, 14):
            result += i
    print(result)

if __name__ == "__main__":
    main()