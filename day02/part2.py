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

def game_power(game_desc: str) -> int:
    min_r, min_g, min_b = 0, 0, 0
    for r, g, b in parse_game(game_desc):
        min_r = max(min_r, r)
        min_g = max(min_g, g)
        min_b = max(min_b, b)
    return min_r * min_g * min_b

def main():
    games = library.read_input(2)
    print(sum(game_power(g) for g in games))

if __name__ == "__main__":
    main()