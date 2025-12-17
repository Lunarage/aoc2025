from typing import Literal, Tuple
import re


def rotate(pos: int, n: int, dir: Literal["L", "R"]) -> Tuple[int, int]:
    newpos = pos
    zeros = 0
    for _ in range(n):
        if dir == "R":
            newpos = (newpos + 1)%100
        if dir == "L":
            newpos = (newpos - 1)%100
        if newpos == 0:
            zeros += 1
    
    return (newpos, zeros)


def main():
    pattern = r'^(?P<dir>L|R)(?P<n>\d+)$'
    pos = 50
    acc = 0

    with open('01/input.txt') as file:
        for line in file:
            match = re.match(pattern, line)
            if not match:
                continue

            dir = match['dir']
            n = int(match['n'])
            (pos, zeros) = rotate(pos, n, dir)
            acc = acc + zeros
            print(dir, n, "=>", pos, zeros, acc)

    print(acc)


if __name__ == "__main__":
    main()
