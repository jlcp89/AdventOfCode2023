import sys
from pathlib import Path
from time import perf_counter
import numpy as np

# Translation table to convert '.' to '0' and '#' to '1'
TR = str.maketrans(".#", "01")

def parse(path):
    def parse_rec(rec):
        return np.array([tuple(map(int, tuple(row))) for row in rec.split()])

    # Read the content of the file at the specified path
    with open(path) as file:
        text = file.read()
        # Split the text into records and parse each record into a NumPy array
        recs = str.translate(text, TR).split("\n\n")
        pats = [parse_rec(rec) for rec in recs]

    return pats

def find_reflection_h(pattern, exclude=0):
    # Find horizontal reflection point for the given pattern
    for i in range(1, pattern.shape[1]):
        if i == exclude:
            continue
        lhs, rhs = np.hsplit(pattern, [i])
        siz = min(lhs.shape[1], rhs.shape[1])
        # Check if the left side, when horizontally flipped, matches the right side
        if (np.fliplr(lhs)[:, :siz] == rhs[:, :siz]).all():
            return i

def find_reflection(pattern, exclude=0):
    # Find reflection point for the given pattern
    r = find_reflection_h(pattern, exclude)
    if r:
        return r

    # If horizontal reflection not found, try vertical reflection
    r = find_reflection_h(np.rot90(pattern), exclude / 100)
    if r:
        return r * 100

    return 0

def solve_part1(data):
    # Calculate the sum of reflection points for each pattern in the data
    return sum([find_reflection(pattern) for pattern in data])

def solve_part2(data):
    sum = 0
    for pattern in data:
        mask = np.zeros_like(pattern)
        base = find_reflection(pattern)
        mask[0, 0] = 1
        # Try different rotations and reflections to find a match
        for i in range(len(pattern.flat)):
            r = find_reflection(pattern ^ np.roll(mask, i), base)
            if r > 0:
                sum += r
                break

    return sum

def main():
    path = Path(sys.argv[1])
    data = parse(path)

    # Measure the time taken for each part of the solution
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    # Print the results and the time taken for each part
    print()
    print(f"part1 : {part1} ")
    print(f"part2 : {part2} ")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
