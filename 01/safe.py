from typing import Literal
import re


def rotate(pos: int, n: int, dir: Literal["L", "R"]) -> int:
    if dir == "R":
        return (pos + n) % 100
    if dir == "L":
        return (pos - n) % 100


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
            pos = rotate(pos, n, dir)
            if pos == 0:
                acc = acc+1

    print(acc)


if __name__ == "__main__":
    main()
