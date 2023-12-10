from common import library

def extrapolate(seq: list[int]) -> int:
    if all(x == 0 for x in seq):
        return 0
    diffs = [y - x for x, y in zip(seq, seq[1:])]
    return seq[-1] + extrapolate(diffs)

def main():
    sequences = [list(map(int, r.split())) for r in library.read_input(9)]
    print(sum(extrapolate(s[::-1]) for s in sequences))

if __name__ == "__main__":
    main()