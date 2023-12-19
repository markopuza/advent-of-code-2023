from common import library
from functools import reduce

def hash(s: str) -> int:
    return reduce(lambda v, ch: (ord(ch) + v)*17%256, s, 0)

def run_sequence(seq: list[str]) -> int:
    boxes = [[] for _ in range(256)]
    for s in seq:
        if '-' in s:
            label, cmnd = s[:-1], '-'
        else:
            label, cmnd = s.split('=')
        
        box = hash(label)
        processed = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                if cmnd == '-':
                    boxes[box] = boxes[box][:i] + boxes[box][i+1:]
                else:
                    boxes[box][i] = (label, int(cmnd))
                processed = True
                break
        if not processed and cmnd != '-':
            boxes[box].append((label, int(cmnd)))
        
    total = 0
    for i, box in enumerate(boxes, 1):
        for j, lens in enumerate(box, 1):
            total += i * j * lens[1]

    return total



def main():
    seq = library.read_input(15)[0].split(',')
    print(run_sequence(seq))


if __name__ == "__main__":
    main()