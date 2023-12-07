# This function takes a mapping and pairs of start and end points.
def translate(mapping, pairs):
    # For each pair of start and end points:
    for start, end in pairs:
        # For each set of mappings (a1, a2, d) in the mapping:
        for a1, a2, d in mapping:
            # Calculate new start and end points based on the mapping.
            yield (start, min(a1, end))
            yield (max(a1, start) + d, min(a2, end) + d)
            # Update the start point.
            start = max(start, min(a2, end))
        # After going through all mappings, yield the final start and end points.
        yield (start, end)

# This function takes mappings and a seed.
def solve(mappings, seed):
    # For each mapping, update the seed based on translations.
    for mapping in mappings:
        seed = [(a, b) for a, b in translate(mapping, seed) if a < b]
    # Return the minimum value from the updated seed.
    return min(a for a, b in seed)

# This function parses input data.
def parse(T, i=3):
    while i < len(T):
        current = []
        # While there's more input data and the line is not empty:
        while i < len(T) and T[i] != '':
            # Extract values from the input line.
            s2, s1, length = (int(x) for x in T[i].split())
            # Append a list with calculated values to the 'current' list.
            current.append([s1, s1 + length, s2 - s1])
            i += 1
        # Yield the 'current' list after sorting it.
        yield sorted(current)
        # Move to the next non-empty line.
        i += 2

# Open the 'seeds.txt' file and read its contents.
with open('seeds.txt', 'r') as file:
    T = file.read().splitlines()

# Extract seed values from the first line of the input.
seeds = [int(x) for x in T[0].split(':')[1].split()]
# Parse the input and store mappings.
mappings = list(parse(T))
# Solve the problem using the provided data.
answer = solve(mappings, ((x, x + y) for x, y in zip(seeds[::2], seeds[1::2])))
# Print the results.
print(answer)
