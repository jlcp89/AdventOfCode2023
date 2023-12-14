# Define possible movement directions using coordinates (N: North, S: South, E: East, W: West)
coords = N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)

# Define a dictionary mapping characters in the grid to their corresponding movement directions
d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

# Open and read the content of the file "d10_real.txt" into a list of strings (grid)
with open("d10_real.txt") as f:
    grid = f.read().strip().splitlines()

# Find the starting position 'S' in the grid
x, y = next(((i, j) for i, s in enumerate(grid) for j, ch in enumerate(s) if ch == "S"), None)

# Initialize a queue (q) with the starting position and its associated part1 value
q = [((x - dx, y - dy), 1) for dx, dy in coords if (dx, dy) in d[grid[x - dx][y - dy]]]

# Initialize a set to keep track of visited positions
visited = {(x, y)}.union(elem[0] for elem in q)

# Perform BFS (Breadth-First Search) to explore the grid and find the shortest path
while q:
    (x, y), part1 = q.pop(0)
    for (dx, dy) in d[grid[x][y]]:
        n = (x + dx, y + dy)
        # Check if the neighbor position is not visited and is not an empty space '.'
        if n not in visited and grid[n[0]][n[1]] != '.':
            q.append((n, part1 + 1))
            visited.add(n)

# Print the result of part 1, which represents the shortest path length
print("Path Length:", part1)
