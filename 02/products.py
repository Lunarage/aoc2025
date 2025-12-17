
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
            if len(id_str) % 2 == 1:
                continue
            half = len(id_str)//2
            left, right = id_str[:half], id_str[half:]
            if left == right:
                id_sum = id_sum + id
    print(id_sum)

if __name__ == "__main__":
    main()
