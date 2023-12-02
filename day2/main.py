import re

def part1():
    total = 0
    for line in open("input.txt", "r"):
        id = int(line.split(":")[0].split(" ")[1])
        sets = line.split(":")[1].strip()

        valid = True
        draws = re.findall("(\d+) (red|green|blue)", sets)

        for count_str, color in draws:
            if ( color == "green" and int(count_str) > 13 ) or \
                ( color == "red" and int(count_str) > 12 ) or \
                ( color == "blue" and int(count_str) > 14 ):
                valid = False
                break

        if valid:
            total += id

    print(f"Part 1 Answer {total}")

def part2():
    total = 0
    for line in open("input.txt", "r"):
        sets = line.split(":")[1].strip()

        draws = re.findall("(\d+) (red|green|blue)", sets)

        red_max = 0
        green_max = 0
        blue_max = 0

        for count_str, color in  draws:
            if color == "green" and int(count_str) > green_max:
                green_max = int(count_str)

            elif color == "blue" and int(count_str) > blue_max:
                blue_max = int(count_str)

            elif color == "red" and int(count_str) > red_max:
                red_max = int(count_str)

        total += (red_max * blue_max * green_max)
    print(f"Part 2 Answer {total}")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()