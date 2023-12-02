def part1():    
    total = 0
    for line in open("input.txt", "r"):
        first_found = False
        second_found = False

        for i in range(len(line)):
            if first_found and second_found:
                break

            if not first_found and line[i].isdigit():
                total += ( 10 * int(line[i]))
                first_found = True

            if not second_found and line[-(i+1)].isdigit():
                total += int(line[-(i+1)])
                second_found = True

    print(f"Part 1 Answer: {total}")

def parse_num(str: str, index: int):
    if str[index].isdigit():
        return int(str[index])
    
    mapping = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    for key, value in zip(mapping.keys(), mapping.values()):
        if str[index:].startswith(key):
            return value

    return -1


def part2():
    total = 0
    for line in open("input.txt", "r").readlines():
        first_found = False
        second_found = False

        for i in range(len(line)):
            if first_found and second_found:
                break

            if not first_found and (value := parse_num(line, i)) > 0:
                total += 10 * value
                first_found = True

            if not second_found and (value := parse_num(line, -(i+1))) > 0:
                total += value
                second_found = True

    print(f"Part 2 Answer: {total}")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()