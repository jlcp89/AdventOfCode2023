# Open the file "d12_real.txt" and read its lines
file = open("d12_real.txt").readlines()

# Initialize an empty list to store records
records = []

# Iterate through each line in the file
for line in file:
    # Remove leading and trailing whitespaces from the line
    line = line.strip()

    # Split the line into pattern and counts based on spaces
    pattern, counts = line.split()

    # Convert the counts string into a tuple of integers
    counts = tuple(int(x) for x in counts.split(","))

    # Append a tuple (pattern, counts) to the records list
    records.append((pattern, counts))

# Function to calculate the arrangements based on a pattern and counts
def calculate_arrangements(pattern: str, counts: tuple[int]) -> int:
    # Base case: if the pattern is empty, return True if counts is also empty
    if not pattern:
        return len(counts) == 0

    # Base case: if counts is empty, return True if "#" is not in the pattern
    if not counts:
        return "#" not in pattern

    # Initialize the result variable
    result = 0

    # Recursive case for patterns starting with "." or "?"
    if pattern[0] in ".?":
        result += calculate_arrangements(pattern[1:], counts)

    # Recursive case for patterns starting with "#"
    if (
        pattern[0] in "#?"
        and counts[0] <= len(pattern)
        and "." not in pattern[: counts[0]]
        and (counts[0] == len(pattern) or pattern[counts[0]] != "#")
    ):
        result += calculate_arrangements(pattern[counts[0] + 1 :], counts[1:])

    # Return the final result
    return result

# Initialize a variable to store the total number of arrangements
total = 0

# Iterate through each record and calculate arrangements
for pattern, counts in records:
    total += calculate_arrangements(pattern, counts)

# Print the total number of arrangements
print(total)
