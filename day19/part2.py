from common import library

Workflow = list[str]

def parse_machine(machine_rows: list[str]) -> tuple[dict[str, Workflow], ...]:
    workflows, parts = {}, []
    ws, ps = '\n'.join(machine_rows).split('\n\n')
    for w in ws.split('\n'):
        rules = w.split('{')[1][:-1].split(',')
        workflows[w.split('{')[0]] = [(r[:2], int(r.split(':')[0][2:]), r.split(':')[1]) if ':' in r else r for r in rules]
    return workflows, None

def get_final_status(workflows: dict[str, Workflow], x: int, m: int, a: int, s: int, current: str = 'in') -> str:
    if current in ('A', 'R'):
        return current 
    for rule in workflows[current]:
        if not isinstance(rule, str):
            left, n, dest = rule
            if {
                'x>': x > n,
                'x<': x < n,
                'm>': m > n,
                'm<': m < n,
                'a>': a > n,
                'a<': a < n,
                's>': s > n,
                's<': s < n,
            }[left]:
                return get_final_status(workflows, x, m, a, s, dest)
        else:
            return get_final_status(workflows, x, m, a, s, rule)

def get_ranges(workflows: dict[str, Workflow]) -> dict[str, tuple[int, int]]:
    ranges = {c: [0, 4000] for c in 'xmas'}
    for w in workflows.values():
        for rule in w:
            for c in 'xmas':
                if rule[0].startswith(c + '>'):
                    ranges[c].append(rule[1])
                elif rule[0].startswith(c + '<'):
                    ranges[c].append(rule[1] - 1)
    return {c: sorted(set(ranges[c])) for c in 'xmas'}

def count_accepted_ranges(ranges: dict[str, tuple[int, int]], workflows: dict[str, Workflow]) -> int:
    total = 0
    for i, (x1, x2) in enumerate(zip(ranges['x'], ranges['x'][1:])):
        print(f'{i + 1}/{-1 + len(ranges["x"])}')
        for m1, m2 in zip(ranges['m'], ranges['m'][1:]):
            for a1, a2 in zip(ranges['a'], ranges['a'][1:]):
                for s1, s2 in zip(ranges['s'], ranges['s'][1:]):
                    total += (get_final_status(workflows, x2, m2, a2, s2) == 'A') * (x2-x1) * (m2-m1) * (a2 - a1) * (s2 - s1)
    return total

def main():
    workflows, _ = parse_machine(library.read_input(19))
    ranges = get_ranges(workflows)
    print(count_accepted_ranges(ranges, workflows))


if __name__ == "__main__":
    main()