from common import library
from functools import reduce

def hash(s: str) -> int:
    return reduce(lambda v, ch: (ord(ch) + v)*17%256, s, 0)

def main():
    seq = library.read_input(15)[0].split(',')
    print(sum(hash(s) for s in seq))


if __name__ == "__main__":
    main()