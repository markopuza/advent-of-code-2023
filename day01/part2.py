import re
from common import library

TEST_VALUES = {
    'two1nine': 29,
    'eightwothree': 83,
    'abcone2threexyz': 13,
    'xtwone3four': 24, 
    '4nineeightseven2': 42,
    'zoneight234': 14, 
    '7pqrstsixteen': 76,
}
SPELLED_OUT_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def calibration_value(s: str) -> int:
    pattern = 'one|two|three|four|five|six|seven|eight|nine|\d'
    matches = re.finditer(f'(?=({pattern}))', s)
    digits =  [match.group(1) for match in matches]
    transform = lambda d: d if re.match(r'\d', d) else SPELLED_OUT_NUMBERS[d]
    first, last = transform(digits[0]), transform(digits[-1])
    return int(f'{first}{last}')
    
def main():
    lines = library.read_input(1)
    print(sum(calibration_value(l) for l in lines))

if __name__ == "__main__":
    for test_string, test_value in TEST_VALUES.items():
        assert calibration_value(test_string) == test_value
    main()