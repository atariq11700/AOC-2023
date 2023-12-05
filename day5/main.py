import re

class Range:
    def __init__(self, dest_start, source_start, len):
        self.dest_start = dest_start
        self.source_start = source_start
        self.len = len

    def __contains__(self, source):
        return source >= self.source_start and source <= self.source_start + self.len
        
    def __getitem__(self, key):
        assert key in self
        return self.dest_start + ( key - self.source_start )
    
class Transform:
    def __init__(self) -> None:
        self.ranges = []
    
    def add_range(self, range):
        self.ranges.append(range)

    def transform(self, value):
        for range in self.ranges:
            if value in range:
                return range[value]
        return value
    
def location(seed, transforms: list[Transform]) -> int:
    loc = seed
    for transform in transforms:
        loc = transform.transform(loc)
    return loc

def part1():
    file = open("input.txt", "r").read()
    sections = file.split("\n\n")

    seeds = re.findall("(\d+)", sections.pop(0))
    transforms: list[Transform] = []

    for i, section in enumerate(sections):
        transforms.append(Transform())
        ranges = re.findall("(\d+) (\d+) (\d+)", section)
        for dest_start, source_start, len in ranges:
            transforms[i].add_range(Range(int(dest_start), int(source_start), int(len)))

    locs = [location(int(seed), transforms) for seed in seeds]

    print(f"Part 1 Answer {min(locs)}")

def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()