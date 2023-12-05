import re
import math

def part1():
    total = 0
    for line in open("input.txt", "r"):
        values = line.split(":")[1].strip()
        winning = set(map(lambda x: int(x.strip()), re.findall("(\d+)", values.split("|")[0])))
        drawn = set(map(lambda x: int(x.strip()), re.findall("(\d+)", values.split("|")[1])))

        selected = winning & drawn

        total += math.pow(2, len(selected) - 1) if len(selected) > 0 else 0

    print(f"Part 1 Answer {int(total)}")

def part2():
    results = {}

    for i, line in enumerate(open("input.txt", "r").readlines()):
        values = line.split(":")[1].strip()
        winning = set(map(lambda x: int(x.strip()), re.findall("(\d+)", values.split("|")[0])))
        drawn = set(map(lambda x: int(x.strip()), re.findall("(\d+)", values.split("|")[1])))

        selected = winning & drawn

        results[i] = list(range(i+1, i+1+len(selected)))

    total = len(results.keys())
    acculmulator_queue = list(results.keys())

    for card in acculmulator_queue:
        total += len(results[card])
        acculmulator_queue.extend(results[card])

    print(f"Part 2 Answer {total}")

if __name__ == "__main__":
    part1()
    part2()