
from typing import List


def nth_largest_index(list: List[int], n: int):
    sorted_list = sorted(list, reverse=True)
    return list.index(sorted_list[n-1])


def n_ordered_largest(joltages: List[int], n: int):
    largest_idx: int
    for i in range(1, n+1):
        largest_idx = nth_largest_index(joltages, i)
        right = joltages[largest_idx+1:]
        if len(right) < (n-1):
            continue
        return [joltages[largest_idx], max(right)]


def main():
    sum = 0
    with open('03/input.txt') as file:
        for line in file:
            joltages = [int(n) for n in line.rstrip()]
            largest = n_ordered_largest(joltages, 2)
            numb = int(str(largest[0]) + str(largest[1]))
            sum += numb
    print(sum)


if __name__ == "__main__":
    main()
