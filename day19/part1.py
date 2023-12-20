from common import library
import re
from dataclasses import dataclass

Workflow = list[str]

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

def parse_machine(machine_rows: list[str]) -> tuple[dict[str, Workflow], list[Part]]:
    workflows, parts = {}, []
    ws, ps = '\n'.join(machine_rows).split('\n\n')
    for w in ws.split('\n'):
        workflows[w.split('{')[0]] = w.split('{')[1][:-1].split(',')
    for p in ps.split('\n'):
        d = {k: int(v) for k, v in re.compile(r'(\w+)=(\d+)').findall(p)}
        parts.append(Part(**d))
    return workflows, parts

def get_final_status(workflows: dict[str, Workflow], part: Part, current: str = 'in') -> str:
    if current in ('A', 'R'):
        return current 
    for rule in workflows[current]:
        if ':' in rule:
            condition, dest = 'part.' + rule.split(':')[0], rule.split(':')[1]
            if eval(condition):
                return get_final_status(workflows, part, dest)
        else:
            return get_final_status(workflows, part, rule)
            

def main():
    workflows, parts = parse_machine(library.read_input(19))
    print(sum(p.x + p.m + p.a + p.s for p in parts if get_final_status(workflows, p) == 'A'))


if __name__ == "__main__":
    main()