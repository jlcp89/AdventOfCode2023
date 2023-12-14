# Function to process input file and extract galaxy information
def process_input(filename):
    # Open the file and read lines
    with open(filename) as file:
        input_data = file.read().splitlines()

    # Get dimensions of the input grid
    x_len = len(input_data[0])
    y_len = len(input_data)

    # Initialize lists to track galaxies along x and y axes
    x_galaxies = [[] for _ in range(x_len)]
    y_galaxies = [[] for _ in range(y_len)]
    galaxy = -1

    # Iterate through each cell in the input grid
    for y, line in enumerate(input_data):
        for x, ch in enumerate(line):
            # If the cell contains '#', mark it as part of a new galaxy
            if ch == '#':
                galaxy += 1
                x_galaxies[x].append(galaxy)
                y_galaxies[y].append(galaxy)

    # Return information about galaxies along x and y axes, and the total number of galaxies
    return x_galaxies, y_galaxies, galaxy


# Function to create a list of galaxies based on the expansion factor
def list_galaxies(expansion):
    galaxies = [None] * (last_galaxy + 1)

    # Process galaxies along the x-axis
    x = 0
    for i in range(len(x_galaxies)):
        galaxy_list = x_galaxies[i]
        if galaxy_list == []:
            x += expansion
        else:
            for galaxy in galaxy_list:
                galaxies[galaxy] = x
            x += 1

    # Process galaxies along the y-axis
    y = 0
    for i in range(len(y_galaxies)):
        galaxy_list = y_galaxies[i]
        if galaxy_list == []:
            y += expansion
        else:
            for galaxy in galaxy_list:
                x = galaxies[galaxy]
                galaxies[galaxy] = (x, y)
            y += 1

    # Return the list of galaxies
    return galaxies


# Function to calculate the sum of Manhattan distances between all pairs of galaxies
def shortest_paths():
    path_sum = 0
    # Iterate through all pairs of galaxies
    for galaxy_a in range(last_galaxy + 1):
        for galaxy_b in range(galaxy_a + 1, last_galaxy + 1):
            # Calculate Manhattan distance and add to the sum
            distance = manhattan_distance(galaxy_a, galaxy_b)
            path_sum += distance
    return path_sum


# Function to calculate the Manhattan distance between two galaxies
def manhattan_distance(gal_a, gal_b):
    ax, ay = galaxies[gal_a]
    bx, by = galaxies[gal_b]
    distance = abs(bx - ax) + abs(by - ay)
    return distance


# Set the filename and expansion factor
filename = 'd11_real.txt'
expansion_factor = 1000000

# Process input to get galaxy information
x_galaxies, y_galaxies, last_galaxy = process_input(filename)

# List galaxies based on the expansion factor
galaxies = list_galaxies(expansion_factor)

# Calculate the sum of Manhattan distances between all pairs of galaxies
path_sum = shortest_paths()

# Print the final path sum
print()
print('Path sum:', path_sum)
