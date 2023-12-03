def part1():
    map = open("input.txt", "r").readlines()
    total = 0
    for y in range(len(map)):    
        processing_number = False
        number = 0
        indicies = []
        for x in range(len(map[y])):
            if processing_number and not map[y][x].isdigit():
                # print(f"Found number {number} ", end="")
                for _x, _y in indicies:
                    if not map[_y][_x].isdigit() and map[_y][_x] != '.' and map[_y][_x] != '\n':
                        # print(f"valid by {map[_y][_x]} at position ({_x},{_y})", end="")
                        total += number
                        break
                # print("\n")
                number = 0
                indicies = []
                processing_number = False

            if map[y][x].isdigit():
                if not processing_number:
                    processing_number = True

                number *= 10
                number += int(map[y][x])

                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if x + dx >= 0 and x + dx < len(map[y]) and y + dy >= 0 and y + dy < len(map):
                            indicies.append((x + dx, y + dy))

    print(f"Part 1 Answer {total}")

def part2():
    map = open("input.txt", "r").readlines()

    gears = {}    
    for y in range(len(map)):
        processing_number = False
        number = 0
        indicies = []
        for x in range(len(map[y])):
            if processing_number and not map[y][x].isdigit():
                for _x, _y in indicies:
                    if map[_y][_x] == '*':
                        if gears.get((_x,_y), None) is None:
                            # print(f"Found potential gear at ({_x}, {_y})")
                            gears[(_x,_y)] = [number]
                        else:
                            # print(f"Updated potential gear at ({_x}, {_y})")
                            gears[(_x,_y)].append(number)
                        break
                number = 0
                indicies = []
                processing_number = False

            if map[y][x].isdigit():
                if not processing_number:
                    processing_number = True

                number *= 10
                number += int(map[y][x])

                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if x + dx >= 0 and x + dx < len(map[y]) and y + dy >= 0 and y + dy < len(map):
                            indicies.append((x + dx, y + dy))

    total = 0
    for values in gears.values():
        if len(values) == 2:
            total += (values[0] * values[1])
    print(f"Part 2 Answer {total}")


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()