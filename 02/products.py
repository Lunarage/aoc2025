
from typing import List


def id_str_invalid(id_str: str) -> bool:
    half = len(id_str)//2
    for size in range(1, half+1):
        # Split string into chunks of size size
        chunks = [id_str[i:i + size] for i in range(0, len(id_str), size)]
        for chunk in chunks:
            if chunks[0] != chunk:
                break
        else:
            return True
    return False
        


def main():
    id_ranges = []
    with open('02/input.txt') as file:
        for line in file:
            id_ranges = [(lambda x: 
                {
                    "start": x.split("-")[0],
                    "end":  x.split("-")[1]
                }
                )(x) for x in line.rstrip().split(",")]

    id_sum = 0
    for id_range in id_ranges:
        start = int(id_range['start'])
        end = int(id_range['end'])
        for id in range(start, end+1):
            id_str = str(id)
            if id_str_invalid(id_str):
                id_sum += id
    print(id_sum)

if __name__ == "__main__":
    main()
