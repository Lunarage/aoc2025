
def check_surround(floor, y, x) -> bool:
    floor_size = {"y": len(floor), "x": len(floor[0])}
    rollcount = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (x+dx < 0 or x+dx > floor_size["x"]-1):
                continue
            if (y+dy < 0 or y+dy > floor_size["y"]-1):
                continue
            if (dx == 0 and dy == 0):
                continue
            if (floor[y+dy][x+dx] == "@"):
                rollcount += 1
    return rollcount < 4


def main():
    floor = []
    accessible = 0
    with open('04/input.txt') as file:
        for line in file:
            floor.append(line.rstrip())
    for y in range(len(floor)):
        for x in range(len(floor[0])):
            if (floor[y][x] == "."):
                print('.', end="")
            elif (check_surround(floor, y, x)):
                accessible += 1
                print('x', end="")
            else:
                print(floor[y][x], end="")
        print('')
    print(accessible)


if __name__ == "__main__":
    main()
