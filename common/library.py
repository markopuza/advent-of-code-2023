from pathlib import Path

def read_input(day: int) -> list[str]:
    with open(f'{Path.cwd()}/day{day:02d}/input.txt') as f:
        return f.readlines()