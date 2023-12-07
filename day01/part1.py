import re
from common import library


def calibration_value(s: str) -> int:
    digits = re.findall(r'\d', s)
    return int(f'{digits[0]}{digits[-1]}')

def main():
    lines = library.read_input(1)
    print(sum(calibration_value(l) for l in lines))

if __name__ == "__main__":
    main()