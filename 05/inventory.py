import re


def main():
    range_pattern = r'(\d+)-(\d+)'
    id_pattern = r'(\d+)'

    fresh_ranges = []
    ingredient_ids = []
    with open('05/input.txt') as file:
        for line in file:
            m = re.search(range_pattern, line)
            if (m):
                fresh_ranges.append(
                    {'start': int(m.group(1)), 'end': int(m.group(2))})
                continue
            m = re.search(id_pattern, line)
            if (m):
                ingredient_ids.append(int(m.group(1)))
                continue

    fresh = 0
    for id in ingredient_ids:
        for frange in fresh_ranges:
            if id >= frange["start"] and id <= frange["end"]:
                fresh += 1
                break
    print(fresh)


if __name__ == "__main__":
    main()
